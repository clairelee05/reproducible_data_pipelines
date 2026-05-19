from pathlib import Path

import pandas as pd

INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")

df = pd.read_csv(INPUT)

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="raise")
df["date"] = df["timestamp"].dt.strftime("%Y-%m-%d")
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)
