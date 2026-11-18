import pandas as pd

game_data = pd.read_csv('video_games_raw.csv')

print('VIDEO GAME CATALOG MANAGER')

#Return the correct data for the game associated with the row number
search_row = int(input('\nEnter a row number to inspect: '))
game = game_data.iloc[search_row]
print('\nSelected Game:')
print(f"Title: {game['Title']}")
print(f"Platform: {game['Platform']}")
print(f"Genre: {game['Genre']}")
print(f"Rating: {game['Rating']}")
print(f"Current Status: {game['Status']}")

#Get a new status and update it to a new file
new_status = input('Enter a new status: ')
game_data.at[search_row, 'Status'] = new_status

#Print the same game with the newly updated status
print('\nStatus updated.')
print(game_data.iloc[search_row][['Title', 'Platform', 'Genre', 'Rating', 'Status']])

#Create the 'Recommended' column and assign the values correctly
game_data['Recommended'] = 'No'
game_data.loc[(game_data['Rating'] >= 8) & (game_data['Price'] <= 40), 'Recommended'] = 'Yes'

recommended_games = game_data.query("Recommended == 'Yes'")
print('\nRecommended Games:')
print(recommended_games[['Title', 'Platform', 'Price', 'Rating']])

game_data.to_csv('video_games_cleaned.csv', index=False)

print('\nThe catalog has been updated.')
print('Saved as video_games_cleaned.csv.')