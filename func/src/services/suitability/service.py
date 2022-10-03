# Jormungandr
from ...domain.models.suitability.model import SuitabilityModel
from ...repositories.mongo_db.suitability.repository import SuitabilityRepository

# Third party
from mnemosine import AsyncCache
from decouple import config


class SuitabilityService:
    @staticmethod
    async def get_latest_questions_with_answers():
        result = await AsyncCache.get(key=config("REDIS_SUITABILITY_KEY"))
        if not result:
            suitability: SuitabilityModel = (
                await SuitabilityRepository.get_latest_suitability()
            )
            result = suitability.get_suitability_response_template()
            await AsyncCache.save(
                key=config("REDIS_SUITABILITY_KEY"),
                value=result,
                time_to_live=eval(config("REDIS_TIME_TO_LIVE")),
            )
        return result
