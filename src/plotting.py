from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np


def main():
    plotGraphsAni()
    # plotGraphs(False)


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

    def get_insert_min(self):
        return self.get_min_count(self.countx, self.county)

    def get_insert_max(self):
        return self.get_max_count(self.countx, self.county)

    def get_insert_average(self):
        return self.get_average_count(self.countx, self.county)

    def get_search_min(self):
        return self.get_min_count(self.searchx, self.searchy)

    def get_search_max(self):
        return self.get_max_count(self.searchx, self.searchy)

    def get_search_average(self):
        return self.get_average_count(self.searchx, self.searchy)

    def get_min_count(self, listx, listy):
        group = listx[0]
        min_value = listy[0]
        min_listx = []
        min_listy = []

        for i in range(len(listx)):
            if group != listx[i]:
                min_listx.append(group)
                min_listy.append(min_value)

                group = listx[i]
                min_value = listy[i]
            else:
                if min_value > listy[i]:
                    min_value = listy[i]

        min_listx.append(group)
        min_listy.append(min_value)

        return min_listx, min_listy

    def get_max_count(self, listx, listy):
        group = listx[0]
        max_value = listy[0]
        max_listx = []
        max_listy = []

        for i in range(len(listx)):
            if group != listx[i]:
                max_listx.append(group)
                max_listy.append(max_value)

                group = listx[i]
                max_value = listy[i]
            else:
                if max_value < listy[i]:
                    max_value = listy[i]

        max_listx.append(group)
        max_listy.append(max_value)

        return max_listx, max_listy

    def get_average_count(self, listx, listy):
        group = listx[0]
        sum = 0
        count = 0
        average_listx = []
        average_listy = []

        for i in range(len(listx)):
            if group != listx[i] and count != 0:
                average_listx.append(group)
                average_listy.append(round(sum / count))

                group = listx[i]
                sum = 0
                count = 0
                sum += listy[i]
                count += 1
            else:
                sum += listy[i]
                count += 1

        average_listx.append(group)
        average_listy.append(round(sum / count))

        return average_listx, average_listy


def plotGraphsAni():
    def update(frame):
        # for each frame, update the data stored on each artist.
        # count plot
        countx = experiment_data.countx[:frame]
        county = experiment_data.county[:frame]
        # search plot
        searchx = experiment_data.searchx[:frame]
        searchy = experiment_data.searchy[:frame]
        # update the scatter plot - count plot
        insert_data = np.stack([countx, county]).T
        insert_scatter.set_offsets(insert_data)
        # min max ave - line plot
        insert_min_plot.set_xdata(insert_min_list[0][:frame])
        insert_min_plot.set_ydata(insert_min_list[1][:frame])
        insert_max_plot.set_xdata(insert_max_list[0][:frame])
        insert_max_plot.set_ydata(insert_max_list[1][:frame])
        insert_ave_plot.set_xdata(insert_ave_list[0][:frame])
        insert_ave_plot.set_ydata(insert_ave_list[1][:frame])
        # search plot
        search_data = np.stack([searchx, searchy]).T
        search_scatter.set_offsets(search_data)
        # min max ave
        search_min_plot.set_xdata(search_min_list[0][:frame])
        search_min_plot.set_ydata(search_min_list[1][:frame])
        search_max_plot.set_xdata(search_max_list[0][:frame])
        search_max_plot.set_ydata(search_max_list[1][:frame])
        search_ave_plot.set_xdata(search_ave_list[0][:frame])
        search_ave_plot.set_ydata(search_ave_list[1][:frame])

        return (insert_scatter, search_scatter, search_min_plot, search_max_plot, search_ave_plot, insert_min_plot,
                insert_max_plot, insert_ave_plot)

    # initialization of plots and settings
    figure, axis = plt.subplots(2, 1, figsize=(10, 8))
    # Grid Setting
    axis[1].grid(True, which="both")
    axis[0].grid(True, which="both")
    # x, y labels and range
    axis[1].set(ylim=[0, 50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
    axis[0].set(ylim=[0, 50], xlabel="Size of AVL Tree", ylabel="Number of comparisons")
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
    axis[1].plot(x_log, y_log, c="purple", label="3 * log (x)")
    axis[0].plot(x_log, y_log, c="purple", label="3 * log (x)")

    # plotting scatter plots for respective search and counts
    insert_scatter = axis[0].scatter(experiment_data.countx[0], experiment_data.county[0], s=10, c='green',
                                     label="count data")
    search_scatter = axis[1].scatter(experiment_data.searchx[0], experiment_data.searchy[0], s=10, c='blue',
                                     label="search data")

    # plotting min max and average
    insert_min_list = experiment_data.get_insert_min()
    insert_min_plot = axis[0].plot(insert_min_list[0][0], insert_min_list[1][0], label="min case")[0]
    insert_max_list = experiment_data.get_insert_max()
    insert_max_plot = axis[0].plot(insert_max_list[0][0], insert_max_list[1][0], label="max case")[0]
    insert_ave_list = experiment_data.get_insert_average()
    insert_ave_plot = axis[0].plot(insert_ave_list[0][0], insert_ave_list[1][0], label="average case")[0]
    # search data
    search_min_list = experiment_data.get_search_min()
    search_min_plot = axis[1].plot(search_min_list[0][0], search_min_list[1][0], label="min case")[0]
    search_max_list = experiment_data.get_search_max()
    search_max_plot = axis[1].plot(search_max_list[0][0], search_max_list[1][0], label="max case")[0]
    search_ave_list = experiment_data.get_search_average()
    search_ave_plot = axis[1].plot(search_ave_list[0][0], search_ave_list[1][0], label="average case")[0]

    # Animation function - uses the update function to animate
    ani = animation.FuncAnimation(fig=figure, func=update, frames=190, interval=1)

    # legends
    axis[0].legend(loc="upper left")
    axis[1].legend(loc="upper left")

    # Displaying plot
    plt.show()


def plotGraphs(save):
    # initialization of plots and settings
    figure, axis = plt.subplots(2, 1, figsize=(10, 8))
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
    axis[1].plot(x_log, y_log, c="purple", label="3 * log (x)")
    axis[0].plot(x_log, y_log, c="purple", label="3 * log (x)")

    # plotting scatter plots for respective search and counts
    axis[0].scatter(experiment_data.countx, experiment_data.county, s=10, c='green', label="count data")
    axis[1].scatter(experiment_data.searchx, experiment_data.searchy, s=10, c='blue', label="search data")

    # plotting min max and average
    insert_min_list = experiment_data.get_insert_min()
    axis[0].plot(insert_min_list[0], insert_min_list[1], label="min case")
    insert_max_list = experiment_data.get_insert_max()
    axis[0].plot(insert_max_list[0], insert_max_list[1], label="max case")
    insert_ave_list = experiment_data.get_insert_average()
    axis[0].plot(insert_ave_list[0], insert_ave_list[1], label="average case")
    # search data
    search_min_list = experiment_data.get_search_min()
    axis[1].plot(search_min_list[0], search_min_list[1], label="min case")
    search_max_list = experiment_data.get_search_max()
    axis[1].plot(search_max_list[0], search_max_list[1], label="max case")
    search_ave_list = experiment_data.get_search_average()
    axis[1].plot(search_ave_list[0], search_ave_list[1], label="average case")

    # legends
    axis[0].legend(loc="upper left")
    axis[1].legend(loc="upper left")

    # just displays the plot or saves the graph as a png
    if save:
        plt.savefig("AVL_comparison_graph.png")
    else:
        plt.show()


if __name__ == '__main__':
    main()
