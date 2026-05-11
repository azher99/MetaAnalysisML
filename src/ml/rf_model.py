from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train_rf(X, y, random_state=42):
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=random_state
)

```
model = RandomForestRegressor(
    n_estimators=300,
    random_state=random_state
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

return {
    "model": model,
    "r2": r2_score(y_test, preds)
}
```