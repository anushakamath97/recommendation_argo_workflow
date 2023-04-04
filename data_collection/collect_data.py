import pandas as pd

movies_df = pd.DataFrame({
    "title_year":[
        "desperate+hours+1990",
        "deranged+1974",
        "one+man+band+2005",
        "the+sadist+1963",
        "the+squaw+man+1914",
    ],
    "title":[
        "Desperate Hours",
        "Deranged",
        "One Man Band",
        "The Sadist",
        "The Squaw Man"
    ],
    "genres": [
        "['Mystery', 'Thriller']",
        "['Crime', 'Horror', 'Thriller']",
        "['Animation', 'Family']",
        "['Horror']",
        "['Western']"
    ]})

movies_df.to_csv("/tmp/movies_data.csv")
