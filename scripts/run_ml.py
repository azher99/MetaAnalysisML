from src.config import *
from src.utils.io import load_data
from src.ml.rf_model import train_rf
from src.utils.plotting import plot_feature_importance

def main():
df = load_data(DATA_PATH)
df = df.dropna()

```
X = df.drop(columns=[Y_COL])
y = df[Y_COL]

result = train_rf(X, y, random_state=RANDOM_STATE)

print("\nR2 score:", result["r2"])

plot_feature_importance(
    result["model"],
    X.columns,
    save_path=OUTPUT_DIR / "feature_importance.png"
)
```

if **name** == "**main**":
main()