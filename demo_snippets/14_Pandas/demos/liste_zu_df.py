import pandas as pd


def main():
    print("DataFrame mit einer Spalte")
    fruechte = ["Apfel", "Birnen", "Kirschen", "Bananen", "Erdbeeren"]
    spalten = ["Frucht"]

    df = pd.DataFrame(fruechte, columns=spalten)
    print(df)

    print(f"\n{42 * '-'}\n\nDataFrame mit mehreren Spalten")
    fruechte = [["Apfel", 1.2], ["Birnen", 1.5], ["Kirschen", 3], ["Bananen", 2], ["Erdbeeren", 3.5]]
    spalten = ["Frucht", "Preis"]

    df = pd.DataFrame(fruechte, columns=spalten)
    print(df)
