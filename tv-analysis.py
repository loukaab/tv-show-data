import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# "id","name","number_of_seasons","number_of_episodes","original_language","vote_count","vote_average","overview","adult",
# "backdrop_path","first_air_date","last_air_date","homepage","in_production","original_name","popularity","poster_path","type",
# "status","tagline","genres","created_by","languages","networks","origin_country","spoken_languages","production_companies",
# "production_countries","episode_run_time"

shows = pd.read_csv("TMDB_tv_dataset_v3.csv")

eshows = shows[shows["vote_count"] > 1000]
#seasons = eshows[eshows["number_of_seasons"]]
#ratings = eshows[eshows["vote_average"]]

plt.scatter(eshows["number_of_seasons"], eshows["vote_average"], alpha=0.3)
plt.show()
