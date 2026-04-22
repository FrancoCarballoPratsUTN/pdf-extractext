from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
import mongomock

def get_mock_repository():
    """Returns a mock MongoRepository instance for testing."""
    mock_repo = MongoRepository()
    mock_repo.collection = mongomock.MongoClient().test_db.test_collection
    return mock_repo
