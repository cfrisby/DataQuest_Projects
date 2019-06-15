import read

if __name__ == "__main__":
    df = read.load_data()
    # df.loc[df['url'].str.count("\.") == 2, 'url'] = df['url'].str.split('.', 1).str[1]
    with pd.option_context('display.max_rows', None):
        print(df['url'].value_counts().head(100))