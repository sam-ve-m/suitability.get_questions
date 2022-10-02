# Jormungandr
from ...domain.models.suitability.model import SuitabilityModel
from ...repositories.mongo_db.suitability.repository import SuitabilityRepository


class SuitabilityService:

    @staticmethod
    async def get_latest_questions_with_answers():
        suitability: SuitabilityModel = await SuitabilityRepository.get_latest_suitability()
        response = suitability.get_suitability_response_template()
        return response
