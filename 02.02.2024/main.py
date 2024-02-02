import matplotlib.pyplot as plt
import csv

X = []
Y = []

with open('data.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')

    for ROWS in plotting:
        X.append(float(ROWS[3]))
        Y.append(float(ROWS[1]))

plt.plot(X, Y)
plt.title('Graph bitcoin price')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()