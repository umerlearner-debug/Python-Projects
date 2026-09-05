import pandas as pd
print('--- PART 1: Pandas Series ---')

scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index = ['NightWolf', 'StarBlaze', 'PixelKing', 'Cyberfox', 'Ironstorm'])
print(players)

print()
print("--- PART 2: PANDAS DATAFRAME ---")

data = (
    'Player': ['NightWolf', 'StarBlaze', 'PixelKing', 'Cyberfox', 'Ironstorm']
    'Level': [42, 38, 35, 30, 27]
    'Score': [98500, 87200, 76400, 65100, 54800]
    'Wins': [210, 185, 162, 140, 118]

)

df = pd.DataFrame(data)
print(df)

print()
print('--- PART 3: ACCESSING ROWS ---')
print('Row 0 (Top player): ')
print(df.loc[0])
print()
print('Rows 2 and 3')
print(df.loc[2:3])

print()
print('--- PART 4: READING A CSV FILE ---')
full_df = pd.read_csv('leaderboard.csv')
print('First five rows (head)')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())

print()
print('--- PART 5: Cleaning Data ---')

print('Rows with missing values removed (dropna):')

clean_df = full_df.dropna()

print(clean_df.to_string())

print()

print('Missing values filled with 0 (fillna):')

filled_df = full_df.fillna(0)

print(filled_df.to_string())