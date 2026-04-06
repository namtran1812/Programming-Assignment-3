import matplotlib.pyplot as plt
sizes = [625, 5625, 15625, 30625, 50625, 62500, 75625, 90000, 105625, 122500]
times = [0.024212332966271788, 0.02217466599540785, 0.026082207972649485, 0.030238917039241642, 0.03581075003603473, 0.038517249980941415, 0.042979583027772605, 0.046439040976110846, 0.052531707973685116, 0.05662925000069663]
plt.plot(sizes, times, marker="o")
plt.xlabel("Input Size (n × m)")
plt.ylabel("Runtime (seconds)")
plt.title("HVLCS Runtime vs Input Size")
plt.grid(True)
plt.savefig("plot_image/runtime_graph.png")
plt.show()