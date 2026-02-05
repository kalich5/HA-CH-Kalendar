from homeassistant.helpers.entity import Entity
from datetime import date


class CHTodaySensor(Entity):

    def __init__(self, data):
        self.data = data


    @property
    def name(self):
        return f"ch_today_{self.data.canton.lower()}"


    @property
    def state(self):

        today = date.today()

        if self.data.is_school_holiday(today):
            return "school_holiday"

        if self.data.is_holiday(today):
            return "holiday"

        return "workday"
