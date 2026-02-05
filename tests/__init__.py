from homeassistant.core import HomeAssistant

DOMAIN = "ch_calendar"

PLATFORMS = ["sensor", "binary_sensor", "calendar"]


async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry):

    from .helpers import CalendarData

    data = CalendarData(hass, entry)

    await data.async_initialize()

    hass.data[DOMAIN][entry.entry_id] = data

    await hass.config_entries.async_forward_entry_setups(
        entry, PLATFORMS
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry):

    await hass.config_entries.async_unload_platforms(
        entry, PLATFORMS
    )

    hass.data[DOMAIN].pop(entry.entry_id)

    return True
