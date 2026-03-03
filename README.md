# CH School & Work Calendar for Home Assistant

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Dynamic calendar and sensors for Swiss public holidays and school vacations, for all 26 cantons.

---

## Features

- **Workday detection** – is today a working day? (not weekend, not public holiday)
- **School day detection** – do children have school? (not weekend, not holiday, not vacation)
- **Public holidays** – including canton-specific holidays and automatic Easter calculation
- **School vacations** – all vacation types per canton (Summer, Autumn, Christmas, Sports/Winter, Spring/Easter)
- **Custom events** – birthdays and family holidays with reminder sensors
- **Calendar entities** – for use in Lovelace calendar cards

---

## Supported vacation types

| Vacation         | Notes                                      |
|------------------|--------------------------------------------|
| Sommerferien     | Summer break, July–August, varies by canton |
| Herbstferien     | Autumn break, October                       |
| Weihnachtsferien | Christmas break, December–January           |
| Sportferien      | Winter/Sport break, February (not all cantons) |
| Frühlingsferien  | Spring/Easter break, relative to Easter    |

---

## Public holidays

Only **1 August (Bundesfeiertag / National Day)** is a federal holiday for all cantons.
All other holidays are set by each canton.

Common holidays (most cantons): New Year, Good Friday, Easter Monday, Ascension, Whit Monday, Christmas.
Catholic cantons additionally observe: Corpus Christi, Assumption, All Saints, Immaculate Conception.
Canton-specific: Geneva Fast (GE), Federal Fast Monday (VD), Knabenschiessen (ZH), Bruder-Klaus (OW), etc.

---

## Installation

### HACS (recommended)
1. Open HACS in Home Assistant
2. Click "Integrations" → three dots → "Custom repositories"
3. Add URL: `https://github.com/kalich5/ch_calendar`
4. Category: "Integration"
5. Search for "CH School & Work Calendar" and install
6. Restart Home Assistant

### Manual
1. Copy `custom_components/ch_calendar` to `<config>/custom_components/`
2. Restart Home Assistant

---

## Configuration

1. Go to **Settings → Devices & Services**
2. Click **"Add Integration"**
3. Search for **"CH School & Work Calendar"**
4. Select your **canton** (for correct vacation dates and public holidays)

### Custom events (birthdays & family holidays)

In the integration options you can enter a list of birthdays and family events.

Format (one per line, or multiple entries separated by `|`):

- `DD.MM | Name` – recurring every year
- `YYYY-MM-DD | Name` – one-time event

Example:
```
15.03 | Birthday Mama | 07.08 | Birthday Papa
2026-12-24 | Special Christmas
```

### Reminder settings
- **reminder_days** – how many days before to start reminders
- **reminder_daily** – repeat reminder every day in the window (or only once)

---

## Entities

### Sensors

| Sensor | Description | Value |
|--------|-------------|-------|
| `sensor.workday` | Is today a working day? | `True` / `False` |
| `sensor.school_day` | Is today a school day? | `True` / `False` |
| `sensor.holiday` | Is today a public holiday? | `True` / `False` |
| `sensor.vacation` | Are there school vacations today? | `True` / `False` |
| `sensor.holiday_name` | Name of today's holiday | text or `None` |
| `sensor.vacation_name` | Name of current vacation | text or `None` |
| `sensor.next_holiday` | Name of next public holiday | text |
| `sensor.days_to_holiday` | Days until next public holiday | number |
| `sensor.next_vacation` | Name of next school vacation | text |
| `sensor.days_to_vacation` | Days until next school vacation | number |
| `sensor.next_birthday` | Name of next birthday | text or `None` |
| `sensor.days_to_birthday` | Days until next birthday | number or `None` |
| `sensor.next_family_holiday` | Name of next family event | text or `None` |
| `sensor.days_to_family_holiday` | Days until next family event | number or `None` |

### Calendars

| Calendar | Description |
|----------|-------------|
| `calendar.swiss_public_holidays` | Canton-specific public holidays |
| `calendar.swiss_school_vacations` | School vacations for your canton |
| `calendar.swiss_holidays_vacations` | Combined calendar |
| `calendar.swiss_custom_events` | Birthdays and family holidays |

---

## Automation examples

### Alarm only on school days
```yaml
automation:
  - alias: "School alarm"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: state
        entity_id: sensor.ch_calendar_school_day
        state: "True"
    action:
      - service: media_player.play_media
        target:
          entity_id: media_player.bedroom
        data:
          media_content_id: "alarm.mp3"
          media_content_type: "music"
```

### Vacation heating mode
```yaml
automation:
  - alias: "Vacation heating mode"
    trigger:
      - platform: state
        entity_id: sensor.ch_calendar_vacation
        to: "True"
    action:
      - service: climate.set_preset_mode
        target:
          entity_id: climate.thermostat
        data:
          preset_mode: "away"
```

### Birthday reminder
```yaml
automation:
  - alias: "Birthday reminder 3 days ahead"
    trigger:
      - platform: numeric_state
        entity_id: sensor.ch_calendar_days_to_birthday
        below: 4
    action:
      - service: notify.mobile_app
        data:
          title: "Birthday coming up!"
          message: >
            In {{ states('sensor.ch_calendar_days_to_birthday') }} days:
            {{ states('sensor.ch_calendar_next_birthday') }}
```

---

## Easter calculation

Easter Sunday is calculated using the Anonymous Gregorian (Computus) algorithm, valid for any year in the Gregorian calendar. The following holidays are derived from it:

- **Good Friday** (Karfreitag) – 2 days before Easter Sunday
- **Easter Monday** (Ostermontag) – 1 day after Easter Sunday
- **Ascension** (Auffahrt) – 39 days after Easter Sunday
- **Whit Monday** (Pfingstmontag) – 50 days after Easter Sunday
- **Corpus Christi** (Fronleichnam) – 60 days after Easter Sunday

---

## License

MIT License
