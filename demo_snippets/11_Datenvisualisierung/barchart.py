import plotly.express as px


def main():
    jahr = [2015, 2016, 2017, 2018, 2019, 2021]
    loc = [1500, 3500, 12000, 9000, 10000, 4000]

    fig = px.bar(x=jahr, y=loc)
    fig.show()


if __name__ == "__main__":
    main()