import pandas as pd

def main():
    fruechte = ["Apfel", "Birnen", "Kirschen", "Bananen", "Erdbeeren"]
    preise = [1.2, 1.5, 3, 2, 3.5]

    # Dict mit Listen
    fruit_dict = {'Frucht': fruechte, 'Preis': preise}

    df = pd.DataFrame(fruit_dict)
    print(df)
