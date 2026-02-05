import json
import os
from datetime import date

BASE = os.path.dirname(os.path.dirname(__file__))

DATA = os.path.join(
    BASE,
    "custom_components",
    "ch_calendar",
    "data",
    "school"
)

CANTONS = {
    "zh","ag","be","bs","bl","lu","sz","zg","sg","gr","ju","ge",
    "fr","ti","vd","vs","sh","ar","ai","nw","ow","tg","ur","ne","so"
}


def test_school_files_exist():

    for year in ["2026", "2027"]:

        path = os.path.join(DATA, f"{year}.json")

        assert os.path.exists(path), f"{year}.json missing"


def test_school_json_valid():

    for year in ["2026", "2027"]:

        with open(os.path.join(DATA, f"{year}.json")) as f:
            data = json.load(f)

        assert isinstance(data, dict)


def test_all_cantons_present():

    for year in ["2026", "2027"]:

        with open(os.path.join(DATA, f"{year}.json")) as f:
            data = json.load(f)

        missing = CANTONS - set(data.keys())

        assert not missing, f"Missing cantons: {missing}"


def test_ranges_valid():

    for year in ["2026", "2027"]:

        with open(os.path.join(DATA, f"{year}.json")) as f:
            data = json.load(f)

        for canton, periods in data.items():

            assert periods, f"{canton} has no holidays"

            for p in periods:

                s = date.fromisoformat(p["start"])
                e = date.fromisoformat(p["end"])

                assert s <= e, f"{canton}: {s}>{e}"
