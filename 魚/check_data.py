from time import sleep
import json
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18, "font.family": "Times New Roman"})
# ------------------ JSONファイルの読み込みをチェック ------------------ #

n = 7
X = []
Q0 = []
Q1 = []
Q2 = []
Q3 = []
Q4 = []
Q5 = []
Q6 = []
with open("./each_timeVSangle.json", 'r') as json_file:
    data = json.load(json_file)
    for row in data:
        X.append(row[0])
        Q0.append(row[1][0])
        Q1.append(row[1][1])
        Q2.append(row[1][2])
        Q3.append(row[1][3])
        Q4.append(row[1][4])
        Q5.append(row[1][5])
        Q6.append(row[1][6])

fig, ax = plt.subplots()
ax.set(xlabel='$time [s]$', ylabel=r'$motor angles [\theta]$')
ax.plot(X, Q0)
ax.plot(X, Q1)
ax.plot(X, Q2)
ax.plot(X, Q3)
ax.plot(X, Q4)
ax.plot(X, Q5)
ax.plot(X, Q6)
plt.show()

# -------------------------------------------------------- #
