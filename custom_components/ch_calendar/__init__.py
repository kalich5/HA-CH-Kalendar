from homeassistant.core import HomeAssistant
from .helpers import CalendarData

DOMAIN = "ch_calendar"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass, entry):
    hass.data[DOMAIN][entry.entry_id] = CalendarData(hass, entry)
    await hass.data[DOMAIN][entry.entry_id].async_initialize()
    return True


async def async_unload_entry(hass, entry):
    hass.data[DOMAIN].pop(entry.entry_id)
    return True