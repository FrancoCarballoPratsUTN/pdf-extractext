from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
import mongomock

def get_mock_repository():
    """Returns a mock MongoRepository instance for testing."""
    collection = mongomock.MongoClient().test_db.test_collection
    mock_repo = MongoRepository(collection)
    mock_repo.collection.create_index("checksum", unique=True)
    return mock_repo
