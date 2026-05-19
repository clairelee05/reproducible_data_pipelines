from pathlib import Path

import pandas as pd

INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")

df = pd.read_csv(INPUT)

row_count_before = len(df)

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="raise")
df["duration_seconds"] = df["duration_seconds"].astype(int)

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"], errors="raise").dt.day_name()

assert len(df) == row_count_before

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)
