"""EDA for dataset"""

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("data01.csv")
profile = ProfileReport(df)

profile.to_file("ProfiledDataset.html")
