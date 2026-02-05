import pytest
from homeassistant.data_entry_flow import FlowResultType


@pytest.mark.asyncio
async def test_config_flow(hass):

    result = await hass.config_entries.flow.async_init(
        "ch_calendar",
        context={"source": "user"},
    )

    assert result["type"] == FlowResultType.FORM

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "canton": "zh",
            "year": 2026
        },
    )

    assert result["type"] == FlowResultType.CREATE_ENTRY
