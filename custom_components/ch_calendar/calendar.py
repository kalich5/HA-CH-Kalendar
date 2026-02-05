from homeassistant.components.calendar import CalendarEntity
from datetime import timedelta


class CHCalendarEntity(CalendarEntity):

    def __init__(self, data):
        self.data = data


    @property
    def name(self):
        return f"ch_calendar_{self.data.canton.lower()}"


    async def async_get_events(self, hass, start_date, end_date):

        events = []

        # státní svátky
        for d, name in self.data.holiday_data.items():

            if start_date <= d <= end_date:
                events.append({
                    "start": d,
                    "end": d + timedelta(days=1),
                    "name": name
                })

        # školní prázdniny
        for ev in self.data.school_data:

            ev_start = ev.begin.date()
            ev_end = ev.end.date()

            if ev_start <= end_date and ev_end >= start_date:
                events.append({
                    "start": ev_start,
                    "end": ev_end + timedelta(days=1),
                    "name": ev.name
                })

        return events
