# Importing packages to be used for data operations below
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# converting an existing CSV file into a DataFrame and changing its column index to match the first column
netflix = pd.read_csv("netflix_data.csv", index_col=0)

# Subset and filter the variables to be used according to the movie type and the year range from 1990 to 1999.
movies = netflix[netflix["type"] == "Movie"]
filtered_movies = movies[np.logical_and(movies["release_year"] >= 1990, movies["release_year"] <= 1999)]

# Creating a histogram plot based on the applied data subset and filters, and customizing the plot
plt.hist(filtered_movies["duration"])
plt.xlabel("Duration (Minutes)")
plt.ylabel("Count Movies")
plt.title('Distribution of Movie Durations in the 1990s')
plt.show()

# Most most frequent movie duration in the 1990s is 100 minutes which More than 40 films

# Subset and filter the variables to be used according to the movie genre action and the year range from 1990 to 1999.
action_movies = movies[movies["genre"] == "Action"]
filtered_action_movies = action_movies[np.logical_and(action_movies["release_year"] >= 1990, action_movies["release_year"] <= 1999)]

# Create variable to count the movies according to filter before
short_movie_count = 0

# Use loop and logic to count the number of short_movie
for lab, row in filtered_action_movies.iterrows() :
    if row["duration"] < 90:
        short_movie_count += 1

# Show the count
print(short_movie_count)



