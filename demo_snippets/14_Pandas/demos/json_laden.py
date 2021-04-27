import pandas as pd


def main(json_file):
    df = pd.read_json(json_file)
    df.to_json("data/neue_json.json", indent=4)

    print(df.describe())

