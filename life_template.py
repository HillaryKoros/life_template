# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:57:02 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:37:31 2024

@author: user
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
import textwrap

# Create figure and axes with increased size
fig, ax = plt.subplots(figsize=(100, 60))

# Hide axes
ax.axis('off')

# Scale factor for reducing the size of the graph elements
scale_factor = 0.75

# Define the scaled positions of the boxes with reduced spacing
positions = {
    "Goal": (0.5, 0.95),
    "Inputs": [(0.2, 0.80), (0.4, 0.80), (0.6, 0.80), (0.8, 0.80)],
    "Activities": [(0.15, 0.60), (0.35, 0.60), (0.55, 0.60), (0.75, 0.60)],
    "Outputs": [(0.3, 0.40), (0.5, 0.40), (0.7, 0.40)],
    "Outcomes": [(0.3, 0.22), (0.5, 0.22), (0.7, 0.22)],
    "Impact": [(0.3, 0.05), (0.5, 0.05), (0.7, 0.05)],
}

# Define the texts in the boxes
texts = {
    "Goal": "Achieve excellence and impactful contributions in the field of geospatial data and information science, " + \
            "entrepreneurship start-ups, and visibility in the job market.",
    "Inputs": [
        "Funding, facilities, technology infrastructure",
        "Trainers, mentors, industry experts",
        "Leadership and influence in the field",
        "Online platform and partnerships"
    ],
    "Activities": [
        "Training sessions",
        "Technological innovation",
        "Networking opportunities",
        "Global collaboration and impact"
    ],
    "Outputs": [
        "Empowered Me",
        "Project development",
        "Publication and dissemination"
    ],
    "Outcomes": [
        "Short-Term: Improved skills and awareness",
        "Medium-Term: Higher job placements, successful start-ups, better retention",
        "Long-Term: Reduced youth unemployment, sustainable growth, resilient workforce"
    ],
    "Impact": [
        "Work-life balance",
        "Successful entrepreneurship start-ups",
        "Personal growth and development"
    ]
}

# Define the scaled sizes of the boxes with smaller dimensions
box_sizes = {
    "Goal": (0.0002 * scale_factor, 0.0002 * scale_factor),  # Further reduce the width and height
    "Inputs": (0.0002 * scale_factor, 0.0002 * scale_factor),  # Further reduce the width and height
    "Activities": (0.0002 * scale_factor, 0.0002 * scale_factor),  # Further reduce the width and height
    "Outputs": (0.0005 * scale_factor, 0.0005 * scale_factor),  # Further reduce the width and height
    "Outcomes": (0.0005 * scale_factor, 0.0005 * scale_factor),  # Further reduce the width and height
    "Impact": (0.0005 * scale_factor, 0.0005 * scale_factor),  # Further reduce the width and height
}

# Define colors for each section
colors = {
    "Goal": "lightgray",
    "Inputs": "lightblue",
    "Activities": "lightgreen",
    "Outputs": "lightcoral",
    "Outcomes": "lightgoldenrodyellow",
    "Impact": "lightpink"
}

# Function to draw boxes with wrapped text
def draw_box(ax, center, text, width, height, color):
    x, y = center
    rect = patches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                  boxstyle="round,pad=0.06", linewidth=0.7, edgecolor="black", facecolor=color, mutation_scale=1, mutation_aspect=1)
    ax.add_patch(rect)

    # Calculate the desired width for text wrapping (adjust as needed)
    wrap_width = 30  # Example: Wrap after 20 characters (you can adjust this value)
    wrapped_text = textwrap.fill(text, wrap_width)  # Wrap the text

    ax.text(x, y, wrapped_text, ha='center', va='center', fontsize=38, fontweight='bold', zorder=20)

# Draw the Goal box
draw_box(ax, positions["Goal"], texts["Goal"], *box_sizes["Goal"], colors["Goal"])

# Draw the Inputs boxes
for pos, text in zip(positions["Inputs"], texts["Inputs"]):
    draw_box(ax, pos, text, *box_sizes["Inputs"], colors["Inputs"])

# Draw the Activities boxes
for pos, text in zip(positions["Activities"], texts["Activities"]):
    draw_box(ax, pos, text, *box_sizes["Activities"], colors["Activities"])

# Draw the Outputs boxes
for pos, text in zip(positions["Outputs"], texts["Outputs"]):
    draw_box(ax, pos, text, *box_sizes["Outputs"], colors["Outputs"])

# Draw the Outcomes boxes
for pos, text in zip(positions["Outcomes"], texts["Outcomes"]):
    draw_box(ax, pos, text, *box_sizes["Outcomes"], colors["Outcomes"])

# Draw the Impact boxes
for pos, text in zip(positions["Impact"], texts["Impact"]):
    draw_box(ax, pos, text, *box_sizes["Impact"], colors["Impact"])

def draw_arrow(ax, start, end):
    ax.add_line(mlines.Line2D([start[0], end[0]], [start[1], end[1]], color='black', linewidth=1.5, zorder=0))
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', mutation_scale=60, color='black', lw=1))

# Draw arrows from Goal to Inputs
for pos in positions["Inputs"]:
    draw_arrow(ax, (positions["Goal"][0], positions["Goal"][1] - 0.060), (pos[0], pos[1] + 0.060))

# Draw arrows from Inputs to Activities
for start in positions["Inputs"]:
    for end in positions["Activities"]:
        draw_arrow(ax, (start[0], start[1] - 0.060), (end[0], end[1] + 0.060))

# Draw arrows from Activities to Outputs
for start in positions["Activities"]:
    for end in positions["Outputs"]:
        draw_arrow(ax, (start[0], start[1] - 0.060), (end[0], end[1] + 0.060))

# Draw arrows from Outputs to Outcomes
for start in positions["Outputs"]:
    for end in positions["Outcomes"]:
        draw_arrow(ax, (start[0], start[1] - 0.060), (end[0], end[1] + 0.060))

# Draw arrows from Outcomes to Impact
for start in positions["Outcomes"]:
    for end in positions["Impact"]:
        draw_arrow(ax, (start[0], start[1] - 0.060), (end[0], end[1] + 0.060))

# Create a legend
legend_elements = [
    patches.Patch(facecolor=colors["Goal"], edgecolor='black', label='Goal'),
    patches.Patch(facecolor=colors["Inputs"], edgecolor='black', label='Inputs'),
    patches.Patch(facecolor=colors["Activities"], edgecolor='black', label='Activities'),
    patches.Patch(facecolor=colors["Outputs"], edgecolor='black', label='Outputs'),
    patches.Patch(facecolor=colors["Outcomes"], edgecolor='black', label='Outcomes'),
    patches.Patch(facecolor=colors["Impact"], edgecolor='black', label='Impact')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=120)

# Show the plot
plt.show()
