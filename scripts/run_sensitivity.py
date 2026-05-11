from src.config import *
from src.utils.io import load_data
from src.meta.sensitivity import leave_one_cluster_out
from src.utils.plotting import plot_loo

def main():
OUTPUT_DIR.mkdir(exist_ok=True)

```
df = load_data(DATA_PATH)
df = df.dropna(subset=[Y_COL, V_COL, CLUSTER_COL])

loo = leave_one_cluster_out(df, Y_COL, V_COL, CLUSTER_COL)

print(loo.head())

plot_loo(
    loo,
    save_path=OUTPUT_DIR / "loo_plot.png"
)
```

if **name** == "**main**":
main()