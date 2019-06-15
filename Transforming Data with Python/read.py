import pandas as pd

def load_data():
    col_names = ["submission_time", "upvotes", "url", "headline"]
    df = pd.read_csv("hn_stories.csv", names=col_names)
    return df

if __name__ == "__main__":
    load_data()