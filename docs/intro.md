# SAW
Explanation:

Data Preparation: Create a DataFrame to store player data and assign weights to each criterion.
Normalization: If necessary, normalize the data to ensure fair comparisons between criteria with different scales.
Weighted Sum Calculation: Calculate the weighted sum for each player by multiplying each criterion's value by its corresponding weight and summing the results.
Ranking: Sort the DataFrame by the weighted score to rank the players.
Additional Considerations:

More Complex MCDA Methods: For more sophisticated decision-making, consider using methods like Analytic Hierarchy Process (AHP) or Technique for Order Preference by Similarity to Ideal Solution (TOPSIS).
Data Quality: Ensure the quality and reliability of the data used in the analysis.
Subjective Factors: Incorporate subjective factors, such as a player's potential, team chemistry, and manager's preferences, into the decision-making process.
Sensitivity Analysis: Perform sensitivity analysis to assess how changes in weights or data affect the final ranking.


# waspas
Explanation:

Data Preparation: Create a pandas DataFrame to store player data and assign weights to each criterion.
Normalization: Normalize the data using min-max normalization to ensure comparability between criteria.
Weighted Sum Calculation: Calculate the weighted sum for each player.
Weighted Product Calculation: Calculate the weighted product for each player.
WASPAS Score Calculation: Combine the weighted sum and weighted product using the lambda coefficient.
Ranking: Rank the players based on their WASPAS scores.
Key Points:

Weighting Coefficient (lambda): This parameter controls the relative importance of the WSM and WPM components. A higher lambda value gives more weight to the WSM.
Normalization: Normalization is crucial to ensure fair comparisons between criteria with different scales.
Criteria Selection: The choice of criteria depends on the specific needs and priorities of the football club.
Weight Assignment: Assigning appropriate weights to criteria is a subjective process that may involve expert judgment or statistical techniques.
Sensitivity Analysis: Perform sensitivity analysis to assess the impact of changes in weights or data on the final rankings.