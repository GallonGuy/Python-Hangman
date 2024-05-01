import random
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(3, 3, figsize=(12, 12), facecolor='lightgray')

for trial in range(1, 10):
    x = random.randint(2, 5000)
    ilist = []
    xlist = []

    print("The initial value of x for trial %s is: %s" % (trial, x))
    i = 1
    while x != 1:
        ilist.append(i)
        xlist.append(int(x))
        i += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1

    print("The total number of iterations of trial %s is %s:" % (trial, i))
    row = (trial - 1) // 3
    col = (trial - 1) % 3
    axs[row, col].plot(ilist, xlist, color='green')

    x_fill = np.array(ilist)
    y_fill = np.array(xlist)

    axs[row, col].fill_between(x_fill, y_fill, np.max(y_fill), facecolor='gray')
    axs[row, col].fill_between(x_fill, y_fill, 0, facecolor='lightgreen', alpha=0.25)
    axs[row, col].set_xlabel('Iteration')
    axs[row, col].set_ylabel('Value of x')
    axs[row, col].set_title('Collatz Conjecture - Trial %s' % trial)

plt.tight_layout()
plt.show()
