import glob
import pandas as pd

dfs = glob.glob('data/data*.csv')
result = pd.concat([pd.read_csv(df) for df in dfs], ignore_index=True)
result.to_csv('data/merge_data.csv', index=False)
