CH_CANTONS = {
    "ZH": ("Zürich", "Schweiz-Zuerich"),
    "BE": ("Bern", "Schweiz-Bern"),
    "LU": ("Luzern", "Schweiz-Luzern"),
    "UR": ("Uri", "Schweiz-Uri"),
    "SZ": ("Schwyz", "Schweiz-Schwyz"),
    "OW": ("Obwalden", "Schweiz-Obwalden"),
    "NW": ("Nidwalden", "Schweiz-Nidwalden"),
    "GL": ("Glarus", "Schweiz-Glarus"),
    "ZG": ("Zug", "Schweiz-Zug"),
    "FR": ("Fribourg", "Schweiz-Freiburg"),
    "SO": ("Solothurn", "Schweiz-Solothurn"),
    "BS": ("Basel-Stadt", "Schweiz-Basel-Stadt"),
    "BL": ("Basel-Land", "Schweiz-Basel-Land"),
    "SH": ("Schaffhausen", "Schweiz-Schaffhausen"),
    "AR": ("Appenzell AR", "Schweiz-Appenzell-Ausserrhoden"),
    "AI": ("Appenzell IR", "Schweiz-Appenzell-Innerrhoden"),
    "SG": ("St. Gallen", "Schweiz-St-Gallen"),
    "GR": ("Graubünden", "Schweiz-Graubuenden"),
    "AG": ("Aargau", "Schweiz-Aargau"),
    "TG": ("Thurgau", "Schweiz-Thurgau"),
    "TI": ("Ticino", "Schweiz-Tessin"),
    "VD": ("Vaud", "Schweiz-Waadt"),
    "VS": ("Valais", "Schweiz-Wallis"),
    "NE": ("Neuchâtel", "Schweiz-Neuenburg"),
    "GE": ("Genève", "Schweiz-Genf"),
    "JU": ("Jura", "Schweiz-Jura")
}


def get_ics_url(code: str) -> str:
    return f"https://www.schulferien.org/iCal/{CH_CANTONS[code][1]}.ics"
