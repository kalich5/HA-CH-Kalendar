from homeassistant.helpers.entity import BinarySensorEntity
from datetime import date

from . import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    data = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([CHWorkdaySensor(data)])



class CHWorkdaySensor(BinarySensorEntity):

    def __init__(self, data):

        self.data = data


    @property
    def name(self):

        return f"ch_workday_{self.data.canton}"


    @property
    def is_on(self):

        today = date.today()

        if today.weekday() >= 5:
            return False

        if self.data.is_school_holiday(today):
            return False

        return not self.data.is_holiday(today)
