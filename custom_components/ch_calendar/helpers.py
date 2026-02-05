import holidays
from ics import Calendar
from datetime import date

from .cantons import CH_CANTONS, get_ics_url


class CalendarData:

    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry

        self.canton = entry.data["canton"]
        self.canton_name = CH_CANTONS[self.canton][0]

        self.holiday_data = holidays.CH(prov=self.canton)
        self.school_data = []


    async def async_initialize(self):
        await self._load_school_holidays()


    async def _load_school_holidays(self):

        url = get_ics_url(self.canton)

        session = self.hass.helpers.aiohttp_client.get_clientsession()

        async with session.get(url) as resp:
            ics_text = await resp.text()

        calendar = Calendar(ics_text)

        self.school_data = list(calendar.events)


    def is_holiday(self, day: date) -> bool:
        return day in self.holiday_data


    def is_school_holiday(self, day: date) -> bool:
        for ev in self.school_data:
            if ev.begin.date() <= day <= ev.end.date():
                return True
        return False
