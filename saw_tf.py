import pandas as pd

# Sample player data (adjust columns as needed)
player_data = {
    'Player': ['Player A', 'Player B', 'Player C'],
    'Skill': [80, 75, 90],
    'Pace': [90, 85, 80],
    'Strength': [70, 80, 75],
    'Age': [25, 28, 23],
    'Cost': [20, 30, 25]
}

# Create a DataFrame
df = pd.DataFrame(player_data)

# Assign weights to each criterion (adjust weights as needed)
weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15, 'Cost': 0.2}

# Normalize the data (optional, if criteria have different scales)
# You can use min-max normalization or z-score normalization

# Calculate the weighted sum for each player
df['Weighted_Score'] = (df['Skill'] * weights['Skill'] +
                        df['Pace'] * weights['Pace'] +
                        df['Strength'] * weights['Strength'] +
                        df['Age'] * weights['Age'] +
                        df['Cost'] * weights['Cost'])

# Rank the players based on the weighted score
df = df.sort_values(by='Weighted_Score', ascending=False)

print(df)