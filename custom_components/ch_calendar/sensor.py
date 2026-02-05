from homeassistant.helpers.entity import Entity
from datetime import date

from . import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    data = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([CHTodaySensor(data)])



class CHTodaySensor(Entity):

    def __init__(self, data):

        self.data = data


    @property
    def name(self):

        return f"ch_today_{self.data.canton}"


    @property
    def state(self):

        today = date.today()

        if self.data.is_school_holiday(today):
            return "school_holiday"


        if self.data.is_holiday(today):
            return "holiday"

        if today.weekday() >= 5:
            return "weekend"

        return "workday"
