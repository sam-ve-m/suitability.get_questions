# Suitability
from ....infrastructures.mongo_db.infrastructure import MongoDBInfrastructure
from ....domain.validators.suitability.validator import SuitabilityValidator
from ....domain.models.suitability.model import SuitabilityModel


# Third party
from decouple import config
from etria_logger import Gladsheim


class SuitabilityRepository(MongoDBInfrastructure):
    @classmethod
    async def _get_collection(cls):
        mongo_client = cls.get_client()
        try:
            database = mongo_client[config("MONGODB_DATABASE_NAME")]
            collection = database[config("MONGODB_SUITABILITY_COLLECTION")]
            return collection
        except Exception as ex:
            Gladsheim.error(
                error=ex, message="Error when trying to get mongo collection"
            )
            raise ex

    @classmethod
    async def get_latest_suitability(cls) -> SuitabilityModel:
        collection = await cls._get_collection()
        suitability = await collection.find_one(
            {"$query": {}, "$orderby": {"version": -1}}
        )
        suitability_validated = SuitabilityValidator(**suitability)
        suitability_model = SuitabilityModel(suitability=suitability_validated)
        return suitability_model


