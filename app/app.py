import pandas as pd


def hello_world():
    df = pd.DataFrame([{"msg": "Hello World!"}])
    return df["msg"][0]


def bye_world():
    return "Bye World!"


if __name__ == "__main__":
    print(hello_world())
