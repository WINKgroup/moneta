import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed()

def replicaMeans(data, size):
    result = []
    for i in range(size):
        result.append(np.random.choice(data, 500).mean())
    return result

df = pd.read_csv('coin.csv', header=None)
series = df[0].map({'testa': 0, 'croce': 1})
means = replicaMeans(series, 1000)
print('Intervallo di confidenza', np.percentile(means, [25, 75]))

notRiggedMeans = []
for i in range(1000):
    notRiggedMeans.append(np.random.binomial(1, .5, 500).mean())

diffMeans = pd.Series(notRiggedMeans) - series.mean()
p1, p2 = np.percentile(diffMeans, [5, 95])
plt.hist(diffMeans, bins = 20, density=True)
plt.axvline(x=0, color='red')
plt.axvline(x=p1, color='green')
plt.axvline(x=p2, color='green')
plt.show()
