from src.config import *
from src.utils.io import load_data
from src.meta.core import random_effects_meta
from src.utils.plotting import forest_plot, funnel_plot
from pathlib import Path

def main():
OUTPUT_DIR.mkdir(exist_ok=True)

```
df = load_data(DATA_PATH)
df = df.dropna(subset=[Y_COL, V_COL])

result = random_effects_meta(df[Y_COL], df[V_COL], alpha=ALPHA)

print("\nMeta-analysis results:")
for k, v in result.items():
    print(f"{k}: {v}")

# Save figures
forest_plot(df, Y_COL, V_COL, result,
            save_path=OUTPUT_DIR / "forest_plot.png")

funnel_plot(df, Y_COL, V_COL,
            save_path=OUTPUT_DIR / "funnel_plot.png")
```

if **name** == "**main**":
main()