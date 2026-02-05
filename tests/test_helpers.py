import pytest
from datetime import date
from custom_components.ch_calendar.helpers import CalendarData


class DummyEntry:
    data = {"canton": "zh", "year": 2026}
    entry_id = "test"


class DummyHass:
    pass


@pytest.mark.asyncio
async def test_helpers_load():

    data = CalendarData(DummyHass(), DummyEntry())

    await data.async_initialize()

    assert data.holidays is not None
    assert data.school_holidays is not None


@pytest.mark.asyncio
async def test_helpers_logic():

    data = CalendarData(DummyHass(), DummyEntry())

    await data.async_initialize()

    # Example: summer holidays
    d = date(2026, 7, 20)

    assert data.is_school_holiday(d) is True
