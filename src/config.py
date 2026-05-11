from pathlib import Path

# -----------------------------
# Paths (Provide data paths)
# -----------------------------

DATA_PATH = Path("data/input_data.xlsx")
OUTPUT_DIR = Path("outputs")

# -----------------------------
# Column names (Edit as needed)
# -----------------------------

Y_COL = "LnRR"
V_COL = "V"
CLUSTER_COL = "paper_id"

# -----------------------------
# Parameters
# -----------------------------

ALPHA = 0.05
RANDOM_STATE = 42
