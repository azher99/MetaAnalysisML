import statsmodels.api as sm

def cluster_robust_intercept(df, y_col, v_col, cluster_col):
y = df[y_col]
w = 1.0 / df[v_col]

```
X = sm.add_constant([1] * len(y))

model = sm.WLS(y, X, weights=w)
result = model.fit(cov_type="cluster", cov_kwds={"groups": df[cluster_col]})

return {
    "coef": result.params[0],
    "se": result.bse[0],
    "p_value": result.pvalues[0]
}
```
