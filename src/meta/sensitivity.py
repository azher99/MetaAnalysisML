import pandas as pd
from .core import random_effects_meta

def leave_one_cluster_out(df, y_col, v_col, cluster_col):
results = []

```
for cl in df[cluster_col].unique():
    d = df[df[cluster_col] != cl]

    fit = random_effects_meta(d[y_col], d[v_col])

    results.append({
        "left_out": cl,
        "mu": fit["mu"],
        "ci_low": fit["ci_low"],
        "ci_high": fit["ci_high"]
    })

return pd.DataFrame(results)
```

def aggregate_effects(df, y_col, v_col, cluster_col):
rows = []

```
for cl, d in df.groupby(cluster_col):
    w = 1.0 / d[v_col]
    y = d[y_col]

    y_bar = (w * y).sum() / w.sum()
    v_bar = 1.0 / w.sum()

    rows.append({
        cluster_col: cl,
        y_col: y_bar,
        v_col: v_bar
    })

return pd.DataFrame(rows)
```
