import pandas as pd


def main(csv_kopf, csv_ohne_kopf):
    # CSV Datei hat Kopfzeile
    print("CSV mit Kopf")
    data = pd.read_csv(csv_kopf, sep='\t')
    df = pd.DataFrame(data)
    print(df)

    # CSV Datei hat keine Kopfzeile
    print(f"\n{42 * '-'}\n\nCSV ohne Kopf")
    data2 = pd.read_csv(csv_ohne_kopf, sep=';', names=['Frucht', 'Preis'])
    df2 = pd.DataFrame(data2)
    print(df2)
