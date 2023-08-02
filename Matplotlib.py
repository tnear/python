# Matplotlib is a comprehensive library for creating static, animated,
# and interactive visualizations in Python.
# https://matplotlib.org/

import matplotlib.pyplot as plt
import numpy as np

def basic():
    # create [0, 6]
    xPoints = [0, 6]

    # create [1, 15]
    yPoints = [1, 15]

    # plot (0, 1) and (6, 15)
    plt.plot(xPoints, yPoints)

    # show figure
    #plt.show()

    # clear current figure for next test
    plt.clf()

def marker():
    # mark points with 'o'. This also shows the line
    # can also use '*', ".', 'x', etc.
    # https://www.w3schools.com/python/matplotlib_markers.asp
    plt.plot([1, 3, 5], [4, 0, 6], marker='o')
    #plt.show()

    plt.clf()

def linestyle():
    # supports 'solid' (default), 'dotted', 'dashed', 'None', and more
    plt.plot([3, 8, 1, 10], linestyle='dotted')
    #plt.show()
    plt.clf()

def multipleLines():
    # plot multiple lines on same figure by calling plt.plot twice
    # this automatically sets the two lines to different colors
    plt.plot([3, 8, 1, 10])
    plt.plot([6, 2, 7, 11])

    #plt.show()
    plt.clf()

def label():
    # Set label for the x- and y-axes
    plt.plot([4, 1, 2])

    # label x-axis
    plt.xlabel('Inputs')
    # label y-axis
    plt.ylabel('Outputs')

    #plt.show()
    plt.clf()

def title():
    plt.plot([1, 2, 3])

    # set the plot title
    plt.title('My plot title')

    #plt.show()
    plt.clf()

def subplot():
    # plot 1
    # 1st arg: num rows, 2nd arg: num cols, 3rd arg: active plot index
    # create 1x2 subplot, where first is active
    plt.subplot(1, 2, 1)
    plt.plot([1, 2])

    # plot 2
    # use 1x2 subplot, make the second active
    plt.subplot(1, 2, 2)
    plt.plot([3, 4])

    # plt.show()
    plt.clf()

# plots one dot for each data point
def scatter():
    x = [[5,7,8,7,2,15,2,9,4,11,12,9,6]]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    plt.scatter(x, y)

    # plt.show()
    plt.clf()

def bar():
    x = ['a', 'b', 'c', 'd']
    y = [3, 8, 1, 10]

    plt.bar(x, y)

    # plt.show()
    plt.clf()

def histogram():
    mean = 170
    std = 10
    numValues = 250

    # create a histogram of heights in centimeters
    x = np.random.normal(mean, std, numValues)
    plt.hist(x)
    #plt.show()
    plt.clf()

def legend():
    plt.plot([1, 4, 3])
    plt.plot([2, 5, 3])

    # Use list of strings corresponding to each line
    plt.legend(['Line 1', 'Line 2'])

    plt.show()
    plt.clf()

def main():
    basic()
    marker()
    linestyle()
    multipleLines()
    label()
    title()
    subplot()
    scatter()
    bar()
    histogram()
    legend()

if __name__ == '__main__':
    main()
    print('Tests passed!')
