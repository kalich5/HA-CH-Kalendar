import voluptuous as vol

from homeassistant import config_entries
from .cantons import CH_CANTONS


class CHCalendarConfigFlow(config_entries.ConfigFlow, domain="ch_calendar"):

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            code = user_input["canton"]
            name = CH_CANTONS[code][0]

            return self.async_create_entry(
                title=f"CH Calendar ({name})",
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("canton"): vol.In(sorted(CH_CANTONS.keys()))
            }),
        )
