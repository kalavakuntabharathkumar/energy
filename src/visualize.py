import matplotlib.pyplot as plt
import pandas as pd

def plot_state(df: pd.DataFrame, state: str, output="energy_trend.png"):
    data = df[df["state"] == state].sort_values("month")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data["month"], data["consumption_mwh"], marker="o")
    ax.set_title(f"Monthly Energy Consumption — {state}")
    ax.set_ylabel("Consumption (MWh)")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(output, dpi=150)
    plt.close(fig)
