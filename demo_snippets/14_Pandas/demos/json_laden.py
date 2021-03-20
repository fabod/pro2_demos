import pandas as pd


def main(json_file):
    df = pd.read_json(json_file)
    print(df)
