'''
Write a program in python to plot a graph for the function y = x^2
'''

from matplotlib import pyplot as plt 
import numpy as np 

def main():
    X_axis = np.arange(-10, 10)
    Y_axis = [x**2 for x in X_axis]

    plt.plot(X_axis, Y_axis)
    plt.xlabel('x')
    plt.ylabel('y=x^2')
    plt.title('Graph of x^2')
    plt.show()
    

if __name__ == "__main__":
    main()