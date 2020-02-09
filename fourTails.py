import numpy as np

fourTails = 0
attempts = 100000
np.random.seed()

for trial in range(attempts):
    tails = np.random.random(size=4) >=.5
    n_tails = np.sum(tails)
    if n_tails == 4:
        fourTails += 1

print('Theory:', .5**4, 'Inference:', fourTails / attempts)