import pandas as pd


def bewerten(num):
    if num <= 1.5:
        return "Billig"
    elif num >= 3:
        return "Teuer"
    else:
        return "Normal"


def main():
    fruechte = [["Apfel", 1.2], ["Birnen", 1.5], ["Kirschen", 3], ["Bananen", 2], ["Erdbeeren", 3.5]]
    df = pd.DataFrame(fruechte, columns=["Frucht", "Preis"])

    df['bewertung'] = df['Preis'].apply(bewerten)
    print(df)



