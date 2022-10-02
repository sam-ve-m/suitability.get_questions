# Jormungandr
from func.src.services.suitability.service import SuitabilityService
from tests.src.services.suitability.stubs import stub_suitability_model

# Standards
from unittest.mock import patch

# Third party
import pytest


@pytest.mark.asyncio
@patch('func.src.services.suitability.service.SuitabilityRepository.get_latest_suitability',
       return_value=stub_suitability_model
       )
async def test_when_success_to_get_suitability_data_then_return_suitability_model(mock_repository):
    suitability = await SuitabilityService.get_latest_questions_with_answers()

    assert isinstance(suitability, dict)
    assert suitability.get("version") == 12
