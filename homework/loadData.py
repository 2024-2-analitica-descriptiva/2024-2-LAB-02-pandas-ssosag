def loadData(name):
    import pandas as pd

    path = "files/input/" + name
    return pd.read_csv(path, sep="\t")
