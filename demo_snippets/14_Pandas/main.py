from demos import liste_zu_df
from demos import dict_zu_df
from demos import csv_laden
from demos import json_laden
from demos import apply
from demos import visualization


def main():
    # csv_laden.main()
    # dict_zu_df.main()
    # csv_laden.main(r'data/csv_mit_kopf.csv', r'data/csv_ohne_kopf.csv')
    json_laden.main(r'data/data.json')
    # apply.main()
    # visualization.main(r'data/pima-indians-diabetes.data.csv')


if __name__ == "__main__":
    main()