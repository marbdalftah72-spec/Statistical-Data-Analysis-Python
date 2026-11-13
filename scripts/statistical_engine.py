import numpy as np
import pandas as pd
from scipy import stats

def compute_summary_statistics(series: pd.Series) -> dict:
    clean = series.dropna()
    return {
        "mean": float(np.mean(clean)),
        "median": float(np.median(clean)),
        "std_dev": float(np.std(clean, ddof=1)),
        "variance": float(np.var(clean, ddof=1)),
        "iqr": float(stats.iqr(clean)),
        "skewness": float(stats.skew(clean)),
        "kurtosis": float(stats.kurtosis(clean)),
        "shapiro_p_value": float(stats.shapiro(clean[:5000])[1]) if len(clean) >= 3 else None
    }
