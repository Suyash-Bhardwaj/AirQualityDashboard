import pandas as pd 

file_path1 = f"E:\\python programs\\__00AQI dashboard\\Data\\air_quality_data.csv"

def clean_data(file_path):

    df = pd.read_csv(file_path)
    print(f"Data loaded: {df.shape[0]} rows,{df.shape[1]} columns")

    df.drop_duplicates()

    df['last_update']= pd.to_datetime(df['last_update'], format="%d-%m-%Y  %H:%M:%S")

    df = df.dropna(subset=['city','pollutant_avg'])

    df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'])

    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

    print("Data cleaned successfully!")
    print(df.head())

    return df


def city_wise_summary(df):
    """Compute average pollution per city."""
    city_summary = (
        df.groupby('city')['pollutant_avg']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("\n🏙️  Top 10 Most Polluted Cities (by average pollutant level):")
    print(city_summary.head(10))
    return city_summary

if __name__ == "__main__":
    df = clean_data("data/air_quality_data.csv")
    summary = city_wise_summary(df)


# df = clean_data(file_path1)
# summary = city_wise_summary(df)


