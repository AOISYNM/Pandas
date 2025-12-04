import matplotlib.pyplot as plt
def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')
    plt.show()
plot_data([1, 2, 3], [4, 5, 6])