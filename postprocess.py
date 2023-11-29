import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the log data
log_file_path = 'logs/game_log.csv'  # Replace with the path to your log file
df = pd.read_csv(log_file_path)

# Analysis 1: Win/Loss/Draw Counts
win_count = df['winner'].value_counts()
loss_count = df['loser'].value_counts()
draw_count = df['draw'].sum()
win_loss_draw = pd.DataFrame({
    'win': win_count,
    'loss': loss_count,
    'draw': [draw_count, draw_count]  
}).fillna(0)
print("Win/Loss/Draw Counts:")
print(win_loss_draw)
print('-'*20)

# Analysis 2: Global Rank
wins = df['winner'].value_counts()
ranks = wins.rank(method='min', ascending=False)
global_ranks = pd.DataFrame({'wins': wins, 'rank': ranks}, dtype=np.int8)
print("Global Ranks:")
print(global_ranks)
print('-'*20)

# Analysis 3: Average Game Duration
average_duration = df['game_duration'].mean()
print(f"Average Game Duration: {average_duration}")


# Plot 1: Win/Loss/Draw Bar Chart
data_for_plot = {
    'X wins': win_loss_draw.loc['X', 'win'],
    'O wins': win_loss_draw.loc['O', 'win'],
    'Draws': win_loss_draw['draw'].sum()
}
plt.bar(data_for_plot.keys(), data_for_plot.values())
plt.title('Game Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.show()

# Plot 2: Game Duration Distribution
plt.hist(df['game_duration'], bins=10, edgecolor='black')
plt.title('Game Duration Distribution')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.show()

# Plot 3: Average Number of Moves
average_durations = df.groupby('winner')['number_of_moves'].mean()
average_durations.plot(kind='bar')
plt.title('Average Number of Moves by Winner')
plt.xlabel('Winner')
plt.ylabel('Average Moves')
plt.xticks(rotation=0)
plt.show()
