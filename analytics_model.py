import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a mock sports dataset (Self-contained so it runs instantly)
raw_data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Kylian Mbappé', 'Erling Haaland', 'Jude Bellingham', 'Kevin De Bruyne', 'Vinicius Jr.'],
    'Team': ['Inter Miami', 'Al Nassr', 'Real Madrid', 'Manchester City', 'Real Madrid', 'Manchester City', 'Real Madrid'],
    'Goals': [25, 28, 31, 35, 18, 9, 21],
    'Assists': [15, 7, 10, 5, 12, 18, 11],
    'Match_Rating': [8.1, 7.8, 8.3, 8.0, 7.9, 8.2, 8.0]
}

df = pd.DataFrame(raw_data)

# 2. Data Analytics: Calculate Total Goal Contributions (Goals + Assists)
df['Contributions'] = df['Goals'] + df['Assists']

# 3. Filter: Find elite players with a Match Rating of 8.0 or higher
elite_players = df[df['Match_Rating'] >= 8.0].sort_values(by='Contributions', ascending=False)

# 4. Print the analytical insights to the terminal
print("==================================================")
print("       DATA ANALYTICS REPORT: ELITE PERFORMERS    ")
print("==================================================")
print(elite_players[['Player', 'Team', 'Contributions', 'Match_Rating']].to_string(index=False))
print("==================================================")

# 5. Data Visualization: Generate a professional performance chart
plt.figure(figsize=(10, 6))
plt.bar(df['Player'], df['Goals'], label='Goals', color='#3498db')
plt.bar(df['Player'], df['Assists'], bottom=df['Goals'], label='Assists', color='#2ecc71')

# Formatting the chart
plt.title('Player Attacking Contributions Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Player Name', fontsize=12)
plt.ylabel('Total Contributions', fontsize=12)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart window
plt.tight_layout()
plt.show()
