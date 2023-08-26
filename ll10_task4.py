import csv

scoreboard = {}

with open('scoreboard.csv') as file1, \
        open('high-score.csv', 'w', newline='') as file2:
    csvreader = csv.DictReader(file1)
    csvwriter = csv.writer(file2)

    for row in csvreader:
        player_name = row['player name']
        score = int(row['score'])

        scoreboard[player_name] = \
            max(scoreboard.get(player_name, score), score)

    csvwriter.writerow(['Player Name', 'High Score'])
    for player_name, high_score in scoreboard.items():
        csvwriter.writerow([player_name, high_score])

print("High scores written to 'high-score.csv'")
