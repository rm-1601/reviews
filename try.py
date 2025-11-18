import plotly.express as px

adv = final_df["ADVRatio"]
count_lt_0005 = (adv < 0.005).sum()
total_trades  = len(adv)
perc_lt_0005  = count_lt_0005 / total_trades * 100

title_text = (f"ADV Ratio Distribution<br>"
              f"Trades with ADVRatio < 0.005: {count_lt_0005} "
              f"({perc_lt_0005:.2f}% of total)")

# Boxplot + all points, horizontal like your seaborn chart
fig = px.box(
    final_df,
    x="ADVRatio",
    points="all",           # show all points (like stripplot)
    title=title_text
)

# x-axis formatting
fig.update_xaxes(
    title="Qty/ADV30 Ratio",
    range=[0, 0.2]
)

# Hide y-axis labels (they're not meaningful here)
fig.update_yaxes(visible=False, showticklabels=False)

# Add vertical line at 0.005
fig.add_vline(
    x=0.005,
    line_dash="dash",
    line_color="red",
    annotation_text="0.005 threshold",
    annotation_position="top left"
)

fig.show()