import matplotlib.pyplot as plt


with open('tuning1.txt') as f:
    freq, step = [float(elem) for elem in f.read().split('\n')]

with open('results1.txt') as f:
    results = f.read().split('\n')
    results = [step * int(elem) for elem in results]

fig, ax = plt.subplots()

ax.plot([freq * i for i in range(len(results))], results)

plt.show()

