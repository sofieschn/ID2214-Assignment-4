"""
Create a clean pipeline overview diagram showing the steps from raw data to predictions.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def create_pipeline_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Colors
    color_input = "#E3F2FD"
    color_extract = "#FFF3E0"
    color_model = "#E8F5E9"
    color_eval = "#F3E5F5"
    color_output = "#E1BEE7"

    # Title
    ax.text(
        5,
        7.5,
        "Machine Learning Pipeline: Molecular Activity Prediction",
        ha="center",
        fontsize=15,
        fontweight="bold",
    )

    # Step 1: Input Data
    input_box = FancyBboxPatch(
        (3.5, 6),
        3,
        0.7,
        boxstyle="round,pad=0.1",
        facecolor=color_input,
        edgecolor="#1976D2",
        linewidth=2,
    )
    ax.add_patch(input_box)
    ax.text(5, 6.35, "Input: SMILES Strings", ha="center", fontsize=11, fontweight="bold")

    # Step 2: Feature Extraction (two paths)
    # Representation A: Descriptors
    desc_box = FancyBboxPatch(
        (0.5, 4),
        2.5,
        1.2,
        boxstyle="round,pad=0.1",
        facecolor=color_extract,
        edgecolor="#F57C00",
        linewidth=2,
    )
    ax.add_patch(desc_box)
    ax.text(1.75, 4.8, "Representation A", ha="center", fontsize=11, fontweight="bold")
    ax.text(1.75, 4.4, "Descriptors &", ha="center", fontsize=10)
    ax.text(1.75, 4.1, "Fragment Features", ha="center", fontsize=10)

    # Representation B: Fingerprints
    fp_box = FancyBboxPatch(
        (7, 4),
        2.5,
        1.2,
        boxstyle="round,pad=0.1",
        facecolor=color_extract,
        edgecolor="#F57C00",
        linewidth=2,
    )
    ax.add_patch(fp_box)
    ax.text(8.25, 4.8, "Representation B", ha="center", fontsize=11, fontweight="bold")
    ax.text(8.25, 4.4, "Morgan", ha="center", fontsize=10)
    ax.text(8.25, 4.1, "Fingerprints", ha="center", fontsize=10)

    # Arrows from input to representations
    arrow1 = FancyArrowPatch(
        (4.2, 6),
        (1.75, 5.2),
        arrowstyle="->",
        mutation_scale=25,
        color="#666",
        linewidth=2.5,
    )
    ax.add_patch(arrow1)

    arrow2 = FancyArrowPatch(
        (5.8, 6),
        (8.25, 5.2),
        arrowstyle="->",
        mutation_scale=25,
        color="#666",
        linewidth=2.5,
    )
    ax.add_patch(arrow2)

    # Step 3: Model Training (for each representation)
    # Descriptors: XGBoost and RF
    xgb_desc_box = FancyBboxPatch(
        (0.5, 2.2),
        2.5,
        0.8,
        boxstyle="round,pad=0.1",
        facecolor=color_model,
        edgecolor="#388E3C",
        linewidth=1.5,
    )
    ax.add_patch(xgb_desc_box)
    ax.text(
        1.75,
        2.6,
        "XGBoost + Random Forest",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )

    # Fingerprints: XGBoost and RF
    xgb_fp_box = FancyBboxPatch(
        (7, 2.2),
        2.5,
        0.8,
        boxstyle="round,pad=0.1",
        facecolor=color_model,
        edgecolor="#388E3C",
        linewidth=1.5,
    )
    ax.add_patch(xgb_fp_box)
    ax.text(
        8.25,
        2.6,
        "XGBoost + Random Forest",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )

    # Arrows from representations to models
    arrow3 = FancyArrowPatch(
        (1.75, 4),
        (1.75, 3),
        arrowstyle="->",
        mutation_scale=25,
        color="#666",
        linewidth=2.5,
    )
    ax.add_patch(arrow3)

    arrow4 = FancyArrowPatch(
        (8.25, 4),
        (8.25, 3),
        arrowstyle="->",
        mutation_scale=25,
        color="#666",
        linewidth=2.5,
    )
    ax.add_patch(arrow4)

    # Step 4: Evaluation
    eval_box = FancyBboxPatch(
        (3.5, 1.5),
        3,
        1,
        boxstyle="round,pad=0.1",
        facecolor=color_eval,
        edgecolor="#7B1FA2",
        linewidth=2,
    )
    ax.add_patch(eval_box)
    ax.text(5, 2.2, "Evaluation", ha="center", fontsize=11, fontweight="bold")
    ax.text(5, 1.9, "Cross-Validation", ha="center", fontsize=9)
    ax.text(5, 1.7, "Model Comparison", ha="center", fontsize=9)

    # Arrows from models to evaluation
    arrow5 = FancyArrowPatch(
        (3, 2.6),
        (3.5, 2.5),
        arrowstyle="->",
        mutation_scale=20,
        color="#666",
        linewidth=2,
    )
    ax.add_patch(arrow5)

    arrow6 = FancyArrowPatch(
        (7, 2.6),
        (6.5, 2.5),
        arrowstyle="->",
        mutation_scale=20,
        color="#666",
        linewidth=2,
    )
    ax.add_patch(arrow6)

    # Step 5: Final Predictions
    output_box = FancyBboxPatch(
        (3.5, 0.2),
        3,
        0.8,
        boxstyle="round,pad=0.1",
        facecolor=color_output,
        edgecolor="#6A1B9A",
        linewidth=2,
    )
    ax.add_patch(output_box)
    ax.text(5, 0.6, "Final Predictions", ha="center", fontsize=11, fontweight="bold")
    ax.text(5, 0.35, "Activity Probability", ha="center", fontsize=9)

    # Arrow from evaluation to output
    arrow7 = FancyArrowPatch(
        (5, 1.5),
        (5, 1),
        arrowstyle="->",
        mutation_scale=25,
        color="#6A1B9A",
        linewidth=2.5,
    )
    ax.add_patch(arrow7)

    # Add labels for clarity
    ax.text(
        1.75,
        5.5,
        "Feature\nExtraction",
        ha="center",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )
    ax.text(
        8.25,
        5.5,
        "Feature\nExtraction",
        ha="center",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    ax.text(
        1.75,
        3.2,
        "Model\nTraining",
        ha="center",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )
    ax.text(
        8.25,
        3.2,
        "Model\nTraining",
        ha="center",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    plt.tight_layout()
    plt.savefig("pipeline_diagram.png", dpi=150, bbox_inches="tight")
    print("Pipeline diagram saved as 'pipeline_diagram.png'")
    plt.show()


if __name__ == "__main__":
    create_pipeline_diagram()

