import read

if __name__ == "__main__":
    df = read.load_data()
    headlines = df['headline'].astype(str).str.cat(sep=" ").lower()
    headline_words = pd.Series(headlines.split())
    print(headline_words.value_counts().head(100))