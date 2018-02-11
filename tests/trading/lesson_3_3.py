"""Create NumPy arrays."""

import numpy as np


def test_run():
    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5,4))    # 5x4 random integer in [0,10)
    print("Array, \n", a)

    # Sum of all elements
    print("Sum of all elements:", a.sum())

    # Iterate over rows, to compute the sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns, to compute the sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean())  # leave out axis arg.


if __name__ == "__main__":
        test_run()
