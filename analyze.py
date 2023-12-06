import pandas as pd
from logic import TicTacToeGame, BotPlayer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def play_game(player1, player2):
    game = TicTacToeGame(player1, player2)
    game.play()

    # Extracting relevant information from the game
    first_move = game.first_move
    game_result = game.game_result
    winner_symbol = game.players[0].symbol if game_result == 'Win' else ('Draw' if game_result == 'Draw' else None)

    return {
        'first_move': first_move,
        'game_result': game_result,
        'winner_symbol': winner_symbol
    }

# Function to simulate multiple games
def simulate_games_and_save(n, file_path):
    results = []
    for _ in range(n):
        player1 = BotPlayer('X')
        player2 = BotPlayer('O')
        result = play_game(player1, player2)
        results.append(result)

    df = pd.DataFrame(results)
    df.to_csv(file_path, index=False)
    return file_path

def analyze_games_from_csv(file_path):
    df = pd.read_csv(file_path)

    df['first_move'] = df['first_move'].apply(lambda x: tuple(map(int, x.strip('()').split(','))))
    df['position_type'] = df['first_move'].apply(lambda x: 'corner' if x in [(0, 0), (0, 2), (2, 0), (2, 2)] else ('center' if x == (1, 1) else 'middle'))
    df['win'] = df['game_result'] == 'Win'
    
    stats = df.groupby('position_type').win.mean()
    X = pd.get_dummies(df['position_type'])
    y = df['win'].astype(int)
    model = LinearRegression()
    model.fit(X, y)
    mse = mean_squared_error(y, model.predict(X))

    return {
        'Descriptive Statistics': stats.to_dict(),
        'Model Coefficients': model.coef_.tolist(),
        'Mean Squared Error': mse
    }

# File path for the CSV
csv_file_path = 'logs/game_results.csv'

# Simulating games, saving to CSV, and analyzing
simulate_games_and_save(30, csv_file_path)
analysis_results = analyze_games_from_csv(csv_file_path)

print(analysis_results)
