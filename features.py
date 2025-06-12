import pandas as pd
import numpy as np
def load_data(csv_path):
  df = pd.read_csv(csv_path)
  return df

def add_features(df):
  df['is_small_amount'] = (df['Amount'] <= 2125.87).astype(int)
  df['log_amount'] = np.log1p(df['Amount'])
  return df
