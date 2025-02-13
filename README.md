# Investigating Netflix Movies

This project explores a dataset of Netflix movies to extract valuable insights. Two key pieces of information are sought:

1. **Identifying the most frequent movie duration** based on movie type and release year range from 1990 to 1999.
2. **Calculating the number of action movies** released between 1990 and 1999 with a duration of under 90 minutes.

## Table of Contents

- [Project Overview](#project-overview)
- [Benefits of this project](#benefits-of-this-project)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Data Description](#data-description)
- [Analysis](#analysis)
- [Results](#results)
- [Conclusion](#conclusion)

## Project Overview

This project aims to analyze a dataset of Netflix movies to gain insights into movie trends during the 1990s. By filtering and subsetting the data, we can identify the most common movie durations for different genres and determine the number of short action movies released within a specific timeframe.

## Benefits of this project

This project offers several benefits derived from the DataCamp Data Science course:

- **Data Manipulation**: Applying data manipulation techniques using libraries like Pandas to filter and subset data based on specific criteria (movie type, release year, duration).
- **Data Analysis**: Performing descriptive statistics to identify trends and patterns, such as the most frequent movie duration.
- **Data Visualization**: Creating visualizations (e.g., histograms) to represent data distributions and communicate findings effectively.
- **Problem-solving**: Developing a structured approach to address specific research questions using data analysis methods.
- **Programming Skills**: Enhancing Python programming skills, particularly in data manipulation and analysis with Pandas.
- **Data Literacy**: Gaining a deeper understanding of how to extract meaningful information from data and use it to answer real-world questions.

## Technologies Used

- Python
- Pandas
- Matplotlib.pyplot
- NumPy

## Data Description

The dataset used in this project is a CSV file named `netflix_data.csv`. It contains information about movies and TV shows available on Netflix. Each row represents a movie or TV show, and the columns include:

*   `show_id`: Unique identifier for each title.
*   `type`: Type of content (Movie or TV Show).
*   `title`: Title of the movie or TV show.
*   `director`: Director of the movie (if applicable).
*   `cast`: Cast of the movie or TV show.
*   `country`: Country where the movie or TV show was produced.
*   `date_added`: Date when the title was added to Netflix.
*   `release_year`: Year when the movie or TV show was released.
*   `duration`: Duration of the movie or TV show (in minutes or seasons).
*   `description`: Brief description of the movie or TV show.
*   `genre`: Genre of the movie or TV show.

## Analysis

The analysis performed in this project involves the following steps:

1.  **Data Loading and Cleaning:** The `netflix_data.csv` file is loaded into a Pandas DataFrame. The data is then cleaned to handle any missing values or inconsistencies.
2.  **Data Filtering:** The data is filtered to include only movies released between 1990 and 1999.
3.  **Duration Analysis:** The distribution of movie durations is analyzed to identify the most frequent duration.
4.  **Action Movie Count:** The number of action movies with a duration of under 90 minutes is calculated.

## Results

The results of the analysis show that the most frequent movie duration for movies released between 1990 and 1999 is 100. Additionally, there are 7 action movies released between 1990 and 1999 with a duration of under 90 minutes.

## Conclusion

This project demonstrates how data analysis techniques can be used to extract insights from a real-world dataset. By filtering and analyzing the Netflix movie data, we were able to identify trends in movie duration and determine the number of short action movies released in the 1990s.