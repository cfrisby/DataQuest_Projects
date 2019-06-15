import dateutil
import read

def extract_hour(timestamp):
    return dateutil.parser.parse(timestamp).hour

if __name__ == "__main__":
    df = read.load_data()
    df['hour_submitted'] = df['submission_time'].apply(extract_hour)
    print(df['hour_submitted'].value_counts())