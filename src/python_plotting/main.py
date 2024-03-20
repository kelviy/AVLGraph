from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

def main():
    # plotGraphsAni()
    plotGraphs(False)

def readCounts(file_count, file_search):
    list_graph_points = ListGraphPoints()

    with open(file_count, "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip().split("\t")
            list_graph_points.add_count_point(eval(line[0]), eval(line[1]))

    with open(file_search, "r") as f:
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

    # initialization of plots and settings
    figure, axis = plt.subplots(2, 1, figsize=(10, 6))
    # Grid Setting
    axis[1].grid(True, which="both")
    axis[0].grid(True, which="both")
    # x, y labels and range
    axis[1].set(ylim = [0,50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[0].set(ylim = [0,50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    # setting titles
    axis[0].set_title("Insert Comparisons")
    axis[1].set_title("Search Comparisons")
    # removes overlap
    plt.tight_layout()

    # loading data
    experiment_data = readCounts("data/insertCount.txt", "data/searchCount.txt")

    # TODO: change log graph to curves of best fit
    # plotting log graphs for both figures
    x_log = np.linspace(1, 50_000, 10_000)
    y_log = 3 * np.log(x_log)
    axis[1].plot(x_log, y_log, c="purple")
    axis[0].plot(x_log, y_log, c="purple")

    # plotting scatter plots for respective search and counts
    insert_scatter = axis[0].scatter(experiment_data.countx[0], experiment_data.county[0], s=10, c='green')
    search_scatter = axis[1].scatter(experiment_data.searchx[0], experiment_data.searchy[0], s=10, c='blue')

    # Animation function - uses the update function to animate
    ani = animation.FuncAnimation(fig=figure, func=update, frames=190, interval=1)

    # Displaying plot
    plt.show()

def plotGraphs(save):
    # initialization of plots and settings
    figure, axis = plt.subplots(2, 1, figsize=(10, 6))
    # Grid Setting
    axis[1].grid(True, which="both")
    axis[0].grid(True, which="both")
    # x, y labels and range
    axis[1].set(ylim=[0, 50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[0].set(ylim=[0, 50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    # setting titles
    axis[0].set_title("Insert Comparisons")
    axis[1].set_title("Search Comparisons")
    # Removes overlap
    plt.tight_layout()

    # loading data
    experiment_data = readCounts("data/insertCount.txt", "data/searchCount.txt")

    # TODO: change log graph to curves of best fit
    # plotting log graphs for both figures
    x_log = np.linspace(1, 50_000, 10_000)
    y_log = 3 * np.log(x_log)
    axis[1].plot(x_log, y_log, c="purple")
    axis[0].plot(x_log, y_log, c="purple")

    # plotting scatter plots for respective search and counts
    axis[0].scatter(experiment_data.countx, experiment_data.county, s=10, c='green')
    axis[1].scatter(experiment_data.searchx, experiment_data.searchy, s=10, c='blue')

    # just displays the plot or saves the graph as a png
    if save:
        plt.savefig("AVL_comparison_graph.png")
    else:
        plt.show()

if __name__ == '__main__':
    main()
