import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
euro_12 = pd.read_csv('Euro_stats.txt', sep=',')

goals = euro_12['Goals']
# print(goals)

# 16 Teams participated in the EURO12!!!!! (ROWS)
# 35 COLMUNS IN THE DATASET

discipline = pd.DataFrame()
discipline['Team'], discipline['Yellow Cards'], discipline['Red Cards'] = euro_12['Team'], euro_12['Yellow Cards'], euro_12['Red Cards']
sort_list = ['Red Cards', 'Yellow Cards']
discipline = discipline.sort_values(by=sort_list, ascending=False)

# print(discipline)


high_goals = euro_12.loc[euro_12['Goals'] > 6]
# print(high_goals)

G_teams = euro_12[euro_12['Team'].str.startswith('G')]
# print(G_teams)

first_7 = euro_12.iloc[:, 0:7]
# print(first_7)

exc_last_3 = euro_12.iloc[:, :-3]
# print(exc_last_3)

E_I_R_accuracy = euro_12.iloc[[3, 7, 12], [0,4]]
# print(E_I_R_accuracy)

euro_12['Passing Accuracy'] = round(euro_12['Passing Accuracy'].str.replace('%', '').astype(float)/100, 2)
euro_12 = euro_12.sort_values(by=['Passing Accuracy'], ascending=False)
print(euro_12['Passing Accuracy'])


