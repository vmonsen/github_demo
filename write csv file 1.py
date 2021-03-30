"""
Write a CSV file with no header row
"""

import csv

players = [
    ['Mickey', 'Mantle,JR', 300],
    ['Hank', 'Aaron', 350],
    ['Roger', 'Marris', 325]]

with open('players1.csv', 'wt', newline='') as file_out:
    csv_out = csv.writer(file_out)
    csv_out.writerows(players)


