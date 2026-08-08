import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# "id","name","number_of_seasons","number_of_episodes","original_language","vote_count","vote_average","overview","adult",
# "backdrop_path","first_air_date","last_air_date","homepage","in_production","original_name","popularity","poster_path","type",
# "status","tagline","genres","created_by","languages","networks","origin_country","spoken_languages","production_companies",
# "production_countries","episode_run_time"

shows = pd.read_csv("TMDB_tv_dataset_v3.csv")

eshows = shows[shows["vote_count"] > 1000]
eshows = eshows.dropna(subset=["vote_count", "number_of_seasons"])
seasonsXrating = eshows[["name", "number_of_seasons","vote_average"]]

season_mean_and_count = seasonsXrating.groupby("number_of_seasons", as_index=False)["vote_average"].agg(["mean", "count"])

# Linear regression
reg = linregress(season_mean_and_count["number_of_seasons"], season_mean_and_count["mean"])
stats = (
    f"y = {reg.slope:.3f}x + {reg.intercept:.3f}\n"
    f"R^2 = {reg.rvalue ** 2:.3f}\n"
    f"P-Value = {reg.pvalue:.3f}"
)

# Make figure
fig, ax = plt.subplots()

ax.plot(season_mean_and_count["number_of_seasons"], reg.intercept +  reg.slope * season_mean_and_count["number_of_seasons"], color="red", linestyle="dashed")
ax.text(0.5, 0.95, stats)

ax.scatter(season_mean_and_count["number_of_seasons"], season_mean_and_count["mean"], alpha=0.3)
ax.set_xlabel("Number of Seasons")
ax.set_ylim(0, 10)
ax.set_ylabel("Average Rating Across All Shows")
ax.set_title("Average TV Series Rating vs Number of Seasons")

plt.show()
