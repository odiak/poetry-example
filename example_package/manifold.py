import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


def generate_quadric_data(N=300):
    X = numpy.zeros((N, 3))
    X[:, 0] = numpy.random.random((N,)) * 2 - 1
    X[:, 1] = numpy.random.random((N,)) * 2 - 1
    X[:, 2] = X[:, 0] ** 2 - X[:, 1] ** 2
    return X


def show_quadric_surface(N=300):
    X = generate_quadric_data(N)

    fig = pyplot.figure()
    ax = Axes3D(fig)
    ax.scatter(*X.T)
    pyplot.show()


if __name__ == "__main__":
    show_quadric_surface()
