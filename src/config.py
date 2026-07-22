from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_FOLDER = ROOT / "input"
OUTPUT_FOLDER = ROOT / "output"

EXCEL_FILE = INPUT_FOLDER / "TIME TABLE JULYTODEC2026.xlsx"
OUTPUT_JSON = OUTPUT_FOLDER / "timetable.json"