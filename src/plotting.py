from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from ListGraphPoints import ListGraphPoints


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

    # plotting log graphs for both figures
    x_log = np.linspace(1, 50_000, 10_000)
    y_log_insert = 3 * np.log(x_log)
    y_log_search = 2 * np.log(x_log)
    axis[0].plot(x_log, y_log_insert, c="blue", label="3 * log (x)", linewidth=10, alpha=0.25)
    axis[1].plot(x_log, y_log_search, c="blue", label="2 * log (x)", linewidth=10, alpha=0.25)

    # alpha=0.6, edgecolors='none' - setting for transparency
    # plotting scatter plots for respective search and counts
    insert_scatter = axis[0].scatter(experiment_data.countx[0], experiment_data.county[0], s=10, c='black',
                                     label="count data")
    search_scatter = axis[1].scatter(experiment_data.searchx[0], experiment_data.searchy[0], s=10, c='black',
                                     label="search data")

    # plotting min max and average
    insert_min_list = experiment_data.get_insert_min()
    insert_min_plot = axis[0].plot(insert_min_list[0][0], insert_min_list[1][0], label="min case", alpha=0.7)[0]
    insert_max_list = experiment_data.get_insert_max()
    insert_max_plot = axis[0].plot(insert_max_list[0][0], insert_max_list[1][0], label="max case", c='red', alpha=0.7)[0]
    insert_ave_list = experiment_data.get_insert_average()
    insert_ave_plot = axis[0].plot(insert_ave_list[0][0], insert_ave_list[1][0], label="average case", c='orange', alpha=0.7)[0]
    # search data
    search_min_list = experiment_data.get_search_min()
    search_min_plot = axis[1].plot(search_min_list[0][0], search_min_list[1][0], label="min case", alpha=0.7)[0]
    search_max_list = experiment_data.get_search_max()
    search_max_plot = axis[1].plot(search_max_list[0][0], search_max_list[1][0], label="max case",c='red', alpha=0.7)[0]
    search_ave_list = experiment_data.get_search_average()
    search_ave_plot = axis[1].plot(search_ave_list[0][0], search_ave_list[1][0], label="average case",c='orange', alpha=0.7)[0]

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

    # plotting log graphs for both figures
    x_log = np.linspace(1, 50_000, 10_000)
    y_log_insert = 3 * np.log(x_log)
    y_log_search = 2 * np.log(x_log)
    axis[0].plot(x_log, y_log_insert, c="blue", label="3 * log (x)", linewidth=10, alpha=0.25)
    axis[1].plot(x_log, y_log_search, c="blue", label="2 * log (x)", linewidth=10, alpha=0.25)

    # alpha=0.6, edgecolors='none' - setting for transparency
    # plotting scatter plots for respective search and counts
    axis[0].scatter(experiment_data.countx, experiment_data.county, s=10, c='black', label="count data")
    axis[1].scatter(experiment_data.searchx, experiment_data.searchy, s=10, c='black', label="search data")

    # plotting min max and average
    insert_min_list = experiment_data.get_insert_min()
    axis[0].plot(insert_min_list[0], insert_min_list[1], label="min case", alpha=0.7)
    insert_max_list = experiment_data.get_insert_max()
    axis[0].plot(insert_max_list[0], insert_max_list[1], label="max case", c='red', alpha=0.7)
    insert_ave_list = experiment_data.get_insert_average()
    axis[0].plot(insert_ave_list[0], insert_ave_list[1], label="average case", c='orange', alpha=0.7)
    # search data
    search_min_list = experiment_data.get_search_min()
    axis[1].plot(search_min_list[0], search_min_list[1], label="min case", alpha=0.7)
    search_max_list = experiment_data.get_search_max()
    axis[1].plot(search_max_list[0], search_max_list[1], label="max case", c='red', alpha=0.7)
    search_ave_list = experiment_data.get_search_average()
    axis[1].plot(search_ave_list[0], search_ave_list[1], label="average case", c='orange', alpha=0.7)

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
