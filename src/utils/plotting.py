import matplotlib.pyplot as plt
import numpy as np

def forest_plot(df, y_col, v_col, overall_result, save_path=None):
y = df[y_col].values
se = np.sqrt(df[v_col].values)

```
ci_low = y - 1.96 * se
ci_high = y + 1.96 * se

fig, ax = plt.subplots(figsize=(6, len(y) * 0.4))

ax.errorbar(y, range(len(y)), xerr=1.96 * se, fmt='o')

ax.axvline(overall_result["mu"], linestyle='--')

ax.set_yticks(range(len(y)))
ax.set_yticklabels(range(len(y)))
ax.set_xlabel("Effect Size (LnRR)")
ax.set_title("Forest Plot")

plt.tight_layout()

if save_path:
    plt.savefig(save_path, dpi=600)

plt.close()
```

def funnel_plot(df, y_col, v_col, save_path=None):
y = df[y_col].values
se = np.sqrt(df[v_col].values)

```
plt.figure(figsize=(5, 6))
plt.scatter(y, se)

plt.gca().invert_yaxis()
plt.xlabel("Effect Size")
plt.ylabel("Standard Error")
plt.title("Funnel Plot")

if save_path:
    plt.savefig(save_path, dpi=600)

plt.close()
```

def plot_feature_importance(model, feature_names, save_path=None):
importances = model.feature_importances_

```
idx = np.argsort(importances)

plt.figure(figsize=(6, 4))
plt.barh(range(len(idx)), importances[idx])
plt.yticks(range(len(idx)), [feature_names[i] for i in idx])
plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")

if save_path:
    plt.savefig(save_path, dpi=600)

plt.close()
```
import matplotlib.pyplot as plt

def plot_loo(loo_df, save_path=None):
plt.figure(figsize=(6, 4))

```
errors = (loo_df["ci_high"] - loo_df["ci_low"]) / 2

plt.errorbar(
    loo_df["mu"],
    range(len(loo_df)),
    xerr=errors,
    fmt='o'
)

plt.yticks(range(len(loo_df)), loo_df["left_out"])
plt.xlabel("Effect Size")
plt.title("Leave-One-Cluster-Out Analysis")

plt.tight_layout()

if save_path:
    plt.savefig(save_path, dpi=600)

plt.close()
```