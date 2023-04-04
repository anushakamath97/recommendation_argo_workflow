import pandas as pd
import sys

from ast import literal_eval

movies_df = pd.read_csv("/tmp/movies_data.csv")[["title_year", "title", "genres"]]

movies_df["genre"] = movies_df["genres"].apply(literal_eval)

movies_df = movies_df.explode("genre")[["title_year", "title", "genre"]]

request = sys.argv[1].strip()

print(movies_df[movies_df["genre"] == request]["title_year"].tolist())
