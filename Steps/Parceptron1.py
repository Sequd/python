import numpy as np


def parceptron_learn_step1():
    # x = np.array([[1, 60], [1, 50], [1, 75]])
    w = np.array([[-5], [-1], [5], [0]])
    x = np.array([[1], [0], [1], [1]])
    step1 = w.T.dot(x)
    print(step1)
    # print(step1.mean(axis=0))

    w = np.array([[5], [0], [-1], [-5]])
    x = np.array([[1], [1], [1], [0]])
    step2 = w.T.dot(x)
    print(step2)
    # print(step2.mean(axis=0))

    w = np.array([[4], [-1], [0], [-1]])
    x = np.array([[1], [0], [0], [0]])
    step3 = w.T.dot(x)
    print(step3)
    # print(step3.mean(axis=0))

    w = np.array([[0], [-10], [5], [2]])
    x = np.array([[1], [1], [0], [0]])
    step4 = w.T.dot(x)
    print(step4)
    # print(step4.mean(axis=0))

    print('Matrix:')
    w = np.array([[-1.5], [1], [1]])
    x = np.array([[1], [1], [1]])
    step5 = w.T.dot(x)

    print(step5)
    # print(step5.mean(axis=0))


parceptron_learn_step1()
