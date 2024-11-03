import pandas as pd

def WASPAS(data, weights, lambda_):
    """
    WASPAS method for football player transfer decision-making.

    Args:
        data: A pandas DataFrame containing player data and criteria.
        weights: A dictionary of weights for each criterion.
        lambda_: A weighting coefficient between 0 and 1.

    Returns:
        A pandas DataFrame with player rankings based on the WASPAS score.
    """

    # Normalize the data (min-max normalization)
    normalized_data = (data - data.min()) / (data.max() - data.min())

    # Calculate the weighted sum (WS)
    ws = normalized_data.mul(weights, axis=1).sum(axis=1)

    # Calculate the weighted product (WP)
    wp = normalized_data.pow(weights, axis=1).prod(axis=1)

    # Calculate the WASPAS score
    waspas_score = lambda_ * ws + (1 - lambda_) * wp

    # Rank the players based on the WASPAS score
    ranked_data = data.copy()
    ranked_data['WASPAS_Score'] = waspas_score
    ranked_data = ranked_data.sort_values(by='WASPAS_Score', ascending=False)

    return ranked_data

# Sample player data
data = {'Player': ['Player A', 'Player B', 'Player C'],
        'Skill': [80, 75, 90],
        'Pace': [90, 85, 80],
        'Strength': [70, 80, 75],
        'Age': [25, 28, 23],
        'Cost': [20, 30, 25]}

df = pd.DataFrame(data)

# Assign weights to criteria
weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15, 'Cost': 0.2}

# Set the weighting coefficient (lambda)
lambda_ = 0.5

# Apply WASPAS
ranked_df = WASPAS(df, weights, lambda_)

print(ranked_df)