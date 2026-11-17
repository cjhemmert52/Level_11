import pandas as pd

game_data = pd.read_csv('video_games_raw.csv')

print('VIDEO GAME CATALOG MANAGER')

search_row = int(input('\nEnter a row number to inspect: '))

print(game_data.iloc[search_row][['Title', 'Platform', 'Genre', 'Rating', 'Status']])

new_status = input('Enter a new status: ')
game_data.at[search_row, 'Status'] = new_status

game_data.to_csv('video_games_raw.csv', index=False)

print('\nStatus updated.')
print(game_data.iloc[search_row][['Title', 'Platform', 'Genre', 'Rating', 'Status']])