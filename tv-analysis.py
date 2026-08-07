import pandas as pd
import matplotlib as plt
import numpy as np

shows = pd.read_csv("TMDB_tv_dataset_v3.csv")

print(f"{shows.describe()}")

