import random
from matplotlib import animation
from src.python_plotting.AVLTree import AVLTree, Data
import matplotlib.pyplot as plt
import numpy as np


def loadData(fileName, N):
    # TODO: make randomised subsets of size N
    with open(fileName, "r") as f:
        lines = f.readlines()
        myTree = AVLTree()
        root = None

        if N != 50000:
            start = random.randint(0, 50000-N)
        else:
            start = 0

        for line in lines[start:start+N]:
            column = line.strip().split("\t")
            data = Data(column[0], column[1], eval(column[2]))
            root = myTree.insert_node(root, data)

        myTree.clear_count()
        return (myTree, root)


def save_insert_count(counts, N):
    #with open("data/insertData.txt", "a") as f:
    with open("insertDataClean.txt", "a") as f:
        for i in counts:
            print(f"{N}\t{i}", file=f)


def save_search_count(counts, N):
    with open("data/searchData.txt", "a") as f:
    # with open("searchDataClean.txt", "a") as f:
        for i in counts:
            print(f"{N}\t{i}", file=f)


def readCounts():
    list_graph_points = ListGraphPoints()
    with open("data/insertCount.txt", "r") as f:
    # with open("insertDataClean.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip().split("\t")
            list_graph_points.add_count_point(eval(line[0]), eval(line[1]))

    #with open("data/searchCount.txt", "r") as f:
    with open("searchDataClean.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip().split("\t")
            list_graph_points.add_search_point(eval(line[0]), eval(line[1]))

    return list_graph_points


class ListGraphPoints:
    def __init__(self):
        self.countx = []
        self.county = []
        self.searchx = []
        self.searchy = []

    def add_count_point(self, x, y):
        self.countx.append(x)
        self.county.append(y)

    def add_search_point(self, x, y):
        self.searchx.append(x)
        self.searchy.append(y)


def plotGraphsAni():
    experiment_data = readCounts()
    figure, axis = plt.subplots(2, 1, figsize=(10, 6))

    x_log = np.linspace(1, 50_000, 10_000)
    y_log = 3 * np.log(x_log)
    axis[1].plot(x_log, y_log, c="purple")
    axis[0].plot(x_log, y_log, c="purple")

    insert_scatter = axis[0].scatter(experiment_data.countx[0], experiment_data.county[0], s=10, c='green')
    search_scatter = axis[1].scatter(experiment_data.searchx[0], experiment_data.searchy[0], s=10, c='blue')

    axis[1].grid(True, which="both")
    axis[0].grid(True, which="both")
    # axis.set_xscale("log")
    axis[1].set(ylim = [0,50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[0].set(ylim = [0,50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[0].set_title("Insert Comparisons")
    axis[1].set_title("Search Comparisons")
    def update(frame):
        # for each frame, update the data stored on each artist.
        x = x_log[:frame]
        countx = experiment_data.countx[:frame]
        county = experiment_data.county[:frame]
        searchx = experiment_data.searchx[:frame]
        searchy = experiment_data.searchy[:frame]
        # update the scatter plot:
        insert_data = np.stack([countx, county]).T
        insert_scatter.set_offsets(insert_data)
        search_data = np.stack([searchx, searchy]).T
        search_scatter.set_offsets(search_data)
        return (insert_scatter, search_scatter)


    ani = animation.FuncAnimation(fig=figure, func=update, frames=150, interval=1)
    #axis.plot()
    plt.tight_layout()

    plt.show()

    # ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
    # plt.savefig("log.png")

def plotGraphs():
    experiment_data = readCounts()
    figure, axis = plt.subplots(2, 1, layout='constrained')

    x_log = np.linspace(1, 50_000, 100_000)
    y_log = 3 * np.log(x_log)
    axis[0].plot(x_log, y_log, c="purple")
    axis[1].plot(x_log, y_log, c="purple")

    axis[0].scatter(experiment_data.countx, experiment_data.county, s=3, c="green")
    axis[1].scatter(experiment_data.searchx, experiment_data.searchy, s=3, c="blue")

    axis[1].grid(True, which="both")
    axis[0].grid(True, which="both")
    axis[0].set_title("Insert Comparisons")
    axis[0].set(xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[1].set_title("Search Comparisons")
    axis[1].set(xlabel="Size of AVL Tree", ylabel="Number of comparisons")


    plt.show()

    # plt.savefig("log.png")


def experiment(N):
    myTreeData, root = loadData("GenericsKB.txt", N)
    search_counts = []
    insert_counts = []

    with open("GenericsKB-queries.txt", "r") as f:
        queries = f.readlines()

    # Search queries
    for i in queries:
        data = Data(i.strip(), None, 0)
        result = myTreeData.search(root, data)
        search_counts.append(myTreeData.get_search_count())

        if result is None:
            root = myTreeData.insert_node(root, data)
            insert_counts.append(myTreeData.get_insert_count())
            root = myTreeData.delete_node(root, data)

        # if result is not None:
        #     print(result.key)
        # else:
        #     print("Value not found")

    save_search_count(search_counts, N)
    save_insert_count(insert_counts, N)

    #Insert Queries
    #
    # for i in queries:
    #     data = Data(i.strip(), None, 0)
    #     root = myTreeData.insert_node(root, data)
    #     insert_counts.append(myTreeData.get_insert_count())
    #     root = myTreeData.delete_node(root, data)
    #
    # save_search_count(insert_counts, N)

def main():
    # fp = open('data/searchData.txt', 'w')
    # fp.close()
    # fp = open('data/insertData.txt', 'w')
    # fp.close()
    #
    # log_range = [10, 100, 1000, 2000, 5000, 10000, 15000, 25000, 43000, 50000]
    # # for i in [10 ** i for i in range(1, 5)]:
    # for i in log_range:
    #     experiment(i)

    plotGraphsAni()

if __name__ == '__main__':
    main()
