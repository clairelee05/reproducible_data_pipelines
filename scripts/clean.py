from pathlib import Path

import pandas as pd

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

VALID_EVENT_TYPES = {
    "click",
    "login",
    "purchase",
    "scroll",
    "view",
}

df = pd.read_csv(INPUT)

df = df.dropna()

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df.dropna(subset=["duration_seconds"])

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]
df = df[df["duration_seconds"] > 0]

df = df[df["duration_seconds"] % 1 == 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)
