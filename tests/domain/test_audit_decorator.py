from app.domain.entities.audit_log import AuditLog
from app.domain.use_cases.audit.audit_decorator import AuditDecorator


class MockUseCase:
    """Mock use case to test the AuditDecorator. It can be configured to return a
    specific value and to assert that it was called with expected arguments.
    - return_value: The value that the execute method will return when called.
    - expected_args: A tuple of expected positional arguments that should be passed
      to the execute method. If provided, the mock asserts the actual arguments match.
    - expected_kwargs: A dictionary of expected keyword arguments that should be passed
      to the execute method. If provided, the mock asserts the keyword arguments match.
    """

    def __init__(self, return_value=None, expected_args=None, expected_kwargs=None):
        self.return_value = return_value
        self.expected_args = expected_args
        self.expected_kwargs = expected_kwargs
        self.executed = False

    def execute(self, *args, **kwargs):
        self.executed = True

        if self.expected_args is not None:
            assert args == self.expected_args
        if self.expected_kwargs is not None:
            assert kwargs == self.expected_kwargs

        return self.return_value


class MockAuditRepository:
    """
    Mock audit repository to capture and inspect saved audit logs.
    """

    def __init__(self):
        self.saved_logs = []

    def save(self, audit_log: AuditLog) -> AuditLog:
        self.saved_logs.append(audit_log)
        return audit_log


def make_decorator(mock_use_case, mock_repo, extractor):
    return AuditDecorator(
        use_case=mock_use_case,
        audit_repo=mock_repo,
        action="test-action",
        entity_type="Document",
        checksum_extractor=extractor,
    )


def test_audit_decorator_executes_use_case_and_saves_log():
    stub_result = type("Result", (), {"checksum": "result-checksum"})()
    mock_use_case = MockUseCase(return_value=stub_result)
    mock_repo = MockAuditRepository()

    decorator = make_decorator(
        mock_use_case, mock_repo, lambda result, *args, **kwargs: result.checksum
    )

    result = decorator.execute()

    assert mock_use_case.executed
    assert len(mock_repo.saved_logs) == 1
    assert mock_repo.saved_logs[0].action == "test-action"
    assert mock_repo.saved_logs[0].entity_type == "Document"
    assert mock_repo.saved_logs[0].checksum == "result-checksum"
    assert result.checksum == "result-checksum"


def test_audit_decorator_uses_kwargs_checksum_when_result_no_checksum():
    mock_use_case = MockUseCase(return_value="plain-result")
    mock_repo = MockAuditRepository()

    decorator = make_decorator(
        mock_use_case,
        mock_repo,
        lambda result, *args, **kwargs: kwargs.get("checksum", ""),
    )

    result = decorator.execute(checksum="kwarg-checksum")

    assert len(mock_repo.saved_logs) == 1
    assert mock_repo.saved_logs[0].checksum == "kwarg-checksum"
    assert result == "plain-result"


def test_audit_decorator_extracts_checksum_from_positional_arg():
    mock_use_case = MockUseCase(
        return_value={"message": "Document deleted successfully."}
    )
    mock_repo = MockAuditRepository()

    decorator = make_decorator(
        mock_use_case, mock_repo, lambda result, *args, **kwargs: args[0]
    )

    decorator.execute("checksum-to-delete")

    assert len(mock_repo.saved_logs) == 1
    assert mock_repo.saved_logs[0].checksum == "checksum-to-delete"


def test_audit_decorator_forwards_args_and_kwargs():
    stub_result = type("Result", (), {"checksum": "cs"})()
    expected_args = ("arg1", "arg2")
    expected_kwargs = {"key": "value"}

    mock_use_case = MockUseCase(
        return_value=stub_result,
        expected_args=expected_args,
        expected_kwargs=expected_kwargs,
    )
    mock_repo = MockAuditRepository()

    decorator = make_decorator(
        mock_use_case, mock_repo, lambda result, *args, **kwargs: result.checksum
    )

    decorator.execute("arg1", "arg2", key="value")
