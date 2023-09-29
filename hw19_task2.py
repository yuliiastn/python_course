import pandas as pd

# Task 2a: Import the dataset and assign it to the 'df' variable
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'  # Replace with the actual dataset URL
df = pd.read_csv(url)

# Task 2b: Select only the 'Team', 'Yellow Cards', and 'Red Cards' columns
selected_columns = ['Team', 'Yellow Cards', 'Red Cards']
subset_df = df[selected_columns]

# Task 2c: Count the number of teams that participated in Euro2012
num_teams_participated = df['Team'].nunique()

# Task 2d: Filter teams that scored more than 6 goals
teams_more_than_6_goals = df[df['Goals'] > 6]

print("Task 2a: Euro2012 Dataset")
print(df)

print("\nTask 2b: Selected Columns (Team, Yellow Cards, Red Cards)")
print(subset_df)

print("\nTask 2c: Number of Teams Participated in Euro2012")
print(num_teams_participated)

print("\nTask 2d: Teams that Scored More Than 6 Goals")
print(teams_more_than_6_goals)
