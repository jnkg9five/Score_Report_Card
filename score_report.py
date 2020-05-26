import os
import csv
from statistics import mean

#CSV lookup#

workdir = os.getcwd()
path = workdir+"//score_report.csv"

scores = []
lookScore = []
lookNameMax = []
lookNameMin = []

with open(path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        scores.append([(row[0]),float(row[1])])

for each in range(len(scores)):
    lookScore.append(scores[each][1])
lookScore = sorted(lookScore)

for each in range(len(scores)):
    if scores[each][1] == max(lookScore):
        lookNameMax.append(scores[each][0])
    if scores[each][1] == min(lookScore):
        lookNameMin.append(scores[each][0])
    else:
        continue
lookNameMax = sorted(lookNameMax)
lookNameMin = sorted(lookNameMin)
        
#For the min and max values, there is a lookup of all the people with the highest and lowest score. 

f = open("score_report.txt", "w")
f.write("\nStatistics about the scores:")
f.write("\nThe average score across the board is "+str(mean(lookScore)))
f.write("\nThe highest score was "+str(max(lookScore))+" from the following people:")
for each in range(len(lookNameMax)):
    f.write("\n"+lookNameMax[each])
f.write("\nThe lowest score was "+str(min(lookScore))+" from the following people:")
for each in range(len(lookNameMin)):
    f.write("\n"+lookNameMin[each])
f.close()

print("Congratulations, a report has been created called score_report.txt")
os.system("pause")