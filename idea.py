from src.data_loader import load_type_chart
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
import numpy as np

# Change the font family and size
plt.rcParams['font.family'] = 'arial'  # You can change 'sans-serif' to other font families like 'serif', 'monospace', etc.
plt.rcParams['font.size'] = 8  # Change the font size to your preference

df = load_type_chart()
pprint(df)

# Define unique values and corresponding colors
unique_values = np.unique(df.values)
num_unique_values = len(unique_values)
colors = ["red", "orange", "yellow", "green"]

# Create a colormap with the defined colors
cmap = sns.color_palette(colors)

# Modify the annotations to include "×" symbol
annot_df = df.applymap(lambda x: f'× {x:.1f}')

# Create a seaborn heatmap
plt.figure(figsize=(8, 6))  # Adjust the figsize as needed
heatmap = sns.heatmap(df, cmap=cmap, annot=annot_df, fmt="", linewidths=2, cbar=False,
                      annot_kws={'fontsize': 7})

# Create a legend with larger custom square markers and labels
legend_labels = {0.0: "No Effect", 0.5: "Not Very Effective", 1.0: "Normal", 2.0: "Super Effective"}

handles = [plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=cmap[i], markersize=10, label=label)
           for i, (value, label) in enumerate(legend_labels.items())]

# Place the legend outside the plot
plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1.05, 1))

# Rotate x-axis labels to 90 degrees
heatmap.xaxis.tick_top()
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)

# plt.title('Seaborn Heatmap with Legend')

# Make the plot layout tight
plt.tight_layout()

plt.show()
