'''
Write a program to plot a bar chart in python to display the result of a school for five consecutive
years.
'''

from matplotlib import pyplot as plt
from random import randint 

def main():
    year = 2014
    Years = list(range(year, year+5))
    Results = sorted([str(randint(90, 100))+'%' for _ in range(len(Years))])
    plt.bar(Years, Results)
    plt.title('School Result of {} years'.format(len(Years)))
    plt.show()
    

if __name__ == "__main__":
    main()