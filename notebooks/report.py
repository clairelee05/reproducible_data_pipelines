import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def __(pd):
    events = pd.read_csv("data/features/events.csv")
    events
    return events,


@app.cell
def __(events, plt):
    fig, ax = plt.subplots()

    ax.hist(events["duration_minutes"].dropna(), bins=20)
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration Minutes")
    ax.set_ylabel("Number of Events")

    fig
    return ax, fig


if __name__ == "__main__":
    app.run()
