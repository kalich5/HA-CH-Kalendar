from homeassistant.helpers.entity import BinarySensorEntity
from datetime import date


class CHWorkdaySensor(BinarySensorEntity):

    def __init__(self, data):
        self.data = data


    @property
    def name(self):
        return f"ch_workday_{self.data.canton.lower()}"


    @property
    def is_on(self):

        today = date.today()

        # víkend = nepracovní den
        if today.weekday() >= 5:
            return False

        return not self.data.is_holiday(today)


class CHSchoolHolidaySensor(BinarySensorEntity):

    def __init__(self, data):
        self.data = data


    @property
    def name(self):
        return f"ch_school_holiday_{self.data.canton.lower()}"


    @property
    def is_on(self):

        today = date.today()

        return self.data.is_school_holiday(today)
