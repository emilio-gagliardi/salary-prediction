import pandas as pd


def hello_world():
    df = pd.DataFrame([{"msg": "Hello World!"}])
    return df["msg"][0]


if __name__ == "__main__":
    print(hello_world())
