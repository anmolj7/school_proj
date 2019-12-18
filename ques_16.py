'''
Write a program in python to plot a pie chart on consumption of water in daily life.
'''
from matplotlib import pyplot as plt 

def main():
    Labels = ['Washing', 'Cooking', 'Drinking', 'Watering Plants']
    Percent = [20, 4, 15, 6]

    plt.pie(Percent, labels=Labels, autopct='%1.1f%%')
    plt.title('Water Consumption In Daily Life.')
    plt.show()

if __name__ == "__main__":
    main()