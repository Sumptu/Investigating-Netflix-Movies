import pandas as pd
import matplotlib.pyplot as plt

# Load Netflix data
netflix_df = pd.read_csv("netflix_data.csv", index_col=0)

# Filter for movies released in the 1990s
movies_1990s = netflix_df[
    (netflix_df['type'] == 'Movie') & 
    (netflix_df['release_year'] >= 1990) & 
    (netflix_df['release_year'] <= 1999)
]

# Visualize the distribution of movie durations in the 1990s
plt.hist(movies_1990s['duration'], bins=20, edgecolor='black')
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Find the most frequent movie duration in the 1990s
most_frequent_duration = movies_1990s['duration'].mode()[0]  
duration = int(most_frequent_duration)  
print(duration)

# Filter for action movies released in the 1990s
condition = netflix_df[
    (netflix_df['type'] == 'Movie') &
    (netflix_df['genre'] == 'Action') &
    (netflix_df['release_year'] >= 1990) & 
    (netflix_df['release_year'] <= 1999)
]

# Count the number of short action movies (duration < 90 minutes)
short_movie_count = 0
for lab, row in condition.iterrows() :
    if row['duration'] < 90 :
        short_movie_count += 1
print(short_movie_count)