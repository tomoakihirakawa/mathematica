from time import sleep
import json
import math
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "Times New Roman", 'font.size': 15})
plt.tight_layout()


def tToi(tIN, w, data_size):
    t = tIN - math.floor(tIN / w)
    i = round(data_size/w*t)
    if i is data_size:
        return 0
    return i

# ------------------ JSONファイルの読み込みをチェック ------------------ #


#% ----------------------- データの読み込み ----------------------- #
n = 7
data_size = 0
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
    timeVSangle = data["timeVSangle"]
    parames = data["params"]
    data_size = len(timeVSangle)
    for row in timeVSangle:
        X.append(row[0])
        Q0.append(row[1][0])
        Q1.append(row[1][1])
        Q2.append(row[1][2])
        Q3.append(row[1][3])
        Q4.append(row[1][4])
        Q5.append(row[1][5])
        Q6.append(row[1][6])
#% -------------------------------------------------------- #
# プロット
fig, ax = plt.subplots()
ax.set(xlabel='time [s]', ylabel='wave height [m]')
ax.plot(X, Q0)
ax.plot(X, Q1)
ax.plot(X, Q2)
ax.plot(X, Q3)
ax.plot(X, Q4)
ax.plot(X, Q5)
ax.plot(X, Q6)
plt.show()

print("Q0 size =", len(Q0))

# ----------------- 時間をインデックスに変換する関数のチェック ---------------- #

print(parames)

r = parames["r"]
w = parames["w"]
L = parames["L"]
c1 = parames["c1"]
c2 = parames["c2"]

T = []
toToiData = []
for i in range(30):
    t = i/10.
    index = tToi(t, w, data_size)
    toToiData.append(index)
    T.append(t)
    print(index, t)

fig, ax = plt.subplots()
ax.set(xlabel='time [s]', ylabel='index of data')
ax.plot(T, toToiData)
plt.show()

# ---------------------- Mathematicaで計算したデータの参照のチェック ---------------------- #

T = []
Qs = [[], [], [], [], [], [], []]
for i in range(200):
    t = i/100.
    index = tToi(t, w, data_size)

    Qs[0].append(Q0[index])
    Qs[1].append(Q1[index])
    Qs[2].append(Q2[index])
    Qs[3].append(Q3[index])
    Qs[4].append(Q4[index])
    Qs[5].append(Q2[index])
    Qs[6].append(Q6[index])

    T.append(t)
    print(index, t)

fig, ax = plt.subplots()
ax.set(xlabel='time [s]', ylabel='servo angle [°]')
for i in range(n):
    ax.plot(T, Qs[i])
plt.show()
