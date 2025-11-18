import plotly.express as px
import plotly.io as pio

# (optional) make sure it renders inside the notebook
pio.renderers.default = "notebook"   # or "notebook_connected"

# --- data + stats ---
notional = final_df["Notional"]

total_trades   = len(notional)
count_le_300   = (notional <= 300).sum()
perc_le_300    = count_le_300 / total_trades * 100

print("Total trades =", total_trades)
print("Number of orders ≤ 300 =", count_le_300)
print(f"Percentage of trades ≤ 300 = {perc_le_300:.2f}%")

# --- title text for the chart ---
title_text = (
    "Notional Distribution (Price × Quantity)<br>"
    f"Trades with Notional ≤ 300: {count_le_300} "
    f"({perc_le_300:.2f}% of total)"
)

# --- interactive histogram ---
fig = px.histogram(
    final_df,
    x="Notional",
    nbins=20,
    title=title_text
)

fig.update_xaxes(title="Notional")
fig.update_yaxes(title="Count")

# vertical line at 300
fig.add_vline(
    x=300,
    line_dash="dash",
    line_color="red",
    annotation_text=f"≤300: {count_le_300} trades",
    annotation_position="top left"
)

fig.update_layout(
    bargap=0.05
)

fig.show()
