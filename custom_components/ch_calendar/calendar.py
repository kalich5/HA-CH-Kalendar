from homeassistant.components.calendar import CalendarEntity
from datetime import timedelta

from . import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    data = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([CHCalendarEntity(data)])



class CHCalendarEntity(CalendarEntity):

    def __init__(self, data):

        self.data = data


    @property
    def name(self):

        return f"ch_calendar_{self.data.canton}"


    async def async_get_events(self, hass, start_date, end_date):

        events = []


        for ev in self.data.get_events(start_date, end_date):

            events.append({
                "start": ev["start"],
                "end": ev["end"] + timedelta(days=1),
                "summary": ev["name"],
            })


        return events
