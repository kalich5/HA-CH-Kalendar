import os
import logging
from datetime import date
from ics import Calendar

_LOGGER = logging.getLogger(__name__)


class CalendarData:

    def __init__(self, hass, entry):

        self.hass = hass
        self.entry = entry

        self.canton = entry.data["canton"]
        self.year = entry.data["year"]

        self.holidays = []


    async def async_initialize(self):

        await self._load_holidays()


    async def _load_holidays(self):

        base = os.path.dirname(__file__)

        filename = f"holidays_{self.canton}_{self.year}.ics"

        path = os.path.join(
            base,
            "data",
            "holidays",
            filename
        )

        if not os.path.exists(path):

            _LOGGER.warning(
                "Holiday file not found: %s", path
            )
            return


        with open(path, "r", encoding="utf-8") as f:

            cal = Calendar(f.read())


        self.holidays = []


        for ev in cal.events:

            self.holidays.append({
                "name": ev.name,
                "start": ev.begin.date(),
                "end": ev.end.date()
            })


    def is_holiday(self, day: date) -> bool:

        for ev in self.holidays:

            if ev["start"] <= day <= ev["end"]:
                return True

        return False


    def get_events(self, start, end):

        result = []

        for ev in self.holidays:

            if ev["start"] <= end and ev["end"] >= start:

                result.append(ev)

        return result
