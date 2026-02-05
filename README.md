# 🇨🇭 HA-CH-Calendar

Home Assistant integrace pro švýcarské státní svátky a školní prázdniny.

Podporuje:
- Všechny kantony (26)
- Offline ICS soubory
- Školní prázdniny (JSON)
- Workday senzor
- Calendar entitu

---

## ✨ Funkce

- 📅 Státní svátky podle kantonu
- 🏫 Školní prázdniny
- 🟢 Pracovní den / volno
- 🔌 Offline (bez API)
- 🔄 Automatické aktualizace přes HACS

---

## 📦 Instalace (HACS – doporučeno)

1. Otevři HACS → Integrations
2. Custom repositories
3. Přidej:

https://github.com/kalich5/HA-CH-Kalendar


4. Kategorie: Integration
5. Nainstaluj **CH Calendar**
6. Restartuj Home Assistant

---

## ⚙️ Nastavení

Po instalaci:

1. Settings → Devices & Services
2. Add Integration
3. Vyber **CH Calendar**
4. Vyber:
   - Kanton
   - Rok

Hotovo.

---

## 📊 Entity

Po instalaci vzniknou:

### Sensor
sensor.ch_today_zh


Možné hodnoty:
- workday
- weekend
- holiday
- school_holiday

### Binary sensor
binary_sensor.ch_workday_zh


True = pracovní den

### Calendar
calendar.ch_calendar_zh


---

## 📁 Datové soubory

### Svátky
custom_components/ch_calendar/data/holidays/
holidays_<canton>_<year>.ics


### Prázdniny
custom_components/ch_calendar/data/school/
2026.json
2027.json


---

## 🔄 Aktualizace dat

Každý rok stačí přidat:

- nové ICS
- nový JSON

Integrace si je načte automaticky.

---

## 🛠 Vývoj

Pull requesty vítány 👍

---

## 📜 Licence

MIT License