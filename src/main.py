from src.AVLTree import AVLTree, Data
import matplotlib.pyplot as plt
import numpy as np

def loadData(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        myTree = AVLTree()
        root = None

        for line in lines:
            column = line.split("\t")
            data = Data(column[0], column[1], column[2])
            root = myTree.insert_node(root, data)

        return [myTree, root]

def f(x):
        return np.log(x)
def plotGraphs():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    x = np.linspace(-10, 10, 1_000)

    plt.plot(x, f(x), color='red')

    plt.show()

def main():
    plotGraphs()


def avlMain():
    myTreeData = loadData("GenericsKB.txt")

    myTreeData[0].printHelper(myTreeData[1], "", True)


if __name__ == '__main__':
    main()
    avlMain()

myTree = AVLTree()
root = None