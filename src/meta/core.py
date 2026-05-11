import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import norm

def weighted_mean(y, w):
return np.sum(w * y) / np.sum(w)

def reml_tau2(y, v):
y = np.asarray(y, dtype=float)
v = np.asarray(v, dtype=float)

```
def objective(tau2):
    w = 1.0 / (v + tau2)
    mu = weighted_mean(y, w)
    return 0.5 * (
        np.sum(np.log(v + tau2))
        + np.log(np.sum(w))
        + np.sum((y - mu) ** 2 * w)
    )

upper = max(1.0, np.var(y, ddof=1) * 10)

res = minimize_scalar(objective, bounds=(0, upper), method="bounded")

return max(0.0, float(res.x))
```

def random_effects_meta(y, v, alpha=0.05):
y = np.asarray(y)
v = np.asarray(v)

```
tau2 = reml_tau2(y, v)

w = 1.0 / (v + tau2)
mu = weighted_mean(y, w)
se = np.sqrt(1.0 / np.sum(w))

# Q statistic
Q = np.sum(w * (y - mu) ** 2)
df = len(y) - 1

# I2
I2 = max(0, (Q - df) / Q) * 100 if Q > 0 else 0

z = norm.ppf(1 - alpha / 2)

return {
    "mu": mu,
    "se": se,
    "ci_low": mu - z * se,
    "ci_high": mu + z * se,
    "tau2": tau2,
    "Q": Q,
    "df": df,
    "I2": I2
}
```