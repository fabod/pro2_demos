import pandas as pd
import matplotlib.pyplot as plt


def main(csv):
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    df = pd.read_csv(csv, names=names)

    df.boxplot()
    df.hist()
    df.groupby("class").hist()
    plt.show()
