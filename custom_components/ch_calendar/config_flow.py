import voluptuous as vol
from homeassistant import config_entries


DOMAIN = "ch_calendar"


CANTONS = {
    "zh": "Zürich",
    "ag": "Aargau",
    "be": "Bern",
    "bs": "Basel-Stadt",
    "bl": "Basel-Land",
    "lu": "Luzern",
    "sz": "Schwyz",
    "zg": "Zug",
    "sg": "St. Gallen",
    "gr": "Graubünden",
    "ju": "Jura",
    "ge": "Genf",
    "fr": "Freiburg",
    "ti": "Tessin",
    "vd": "Waadt",
    "vs": "Wallis",
    "sh": "Schaffhausen",
    "ar": "Appenzell AR",
    "ai": "Appenzell IR",
    "nw": "Nidwalden",
    "ow": "Obwalden",
    "tg": "Thurgau",
    "ur": "Uri",
    "ne": "Neuenburg"
}


class CHCalendarConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN
):

    async def async_step_user(self, user_input=None):

        if user_input is not None:

            return self.async_create_entry(
                title=f"CH Calendar ({CANTONS[user_input['canton']]})",
                data=user_input
            )


        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({

                vol.Required("canton"):
                    vol.In(CANTONS),

                vol.Required("year", default=2026):
                    int,

            }),
        )
