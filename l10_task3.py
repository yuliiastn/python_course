import random 
import csv


def sim_score(players=list, rounds=int):
    players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
    scores = []
    for i in range(1, 101):
        for player in players:
            score = random.randint(0, 1000)
            scores.append([player, score])
    return scores


result = sim_score()

with open('scoreboard.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    header = ['player name', 'score']
    writer.writerow(header)
    writer.writerows(result)
