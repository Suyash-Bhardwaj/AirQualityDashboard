import pandas as pd
import matplotlib.pyplot as plt
from scripts.process_data import city_wise_summary,clean_data 


def plot_top_cities(df, top_n=10):
    """Plot the top N most polluted cities."""
    # Step 1: Compute summary
    city_summary = (
        df.groupby('city')['pollutant_avg']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    # Step 2: Take top N
    top_cities = city_summary.head(top_n)

    # Step 3: Plot
    plt.figure(figsize=(10, 6))
    plt.barh(top_cities['city'], top_cities['pollutant_avg'], color='crimson')
    plt.xlabel("Average Pollutant Level")
    plt.ylabel("City")
    plt.title(f"Top {top_n} Most Polluted Cities in India")
    plt.gca().invert_yaxis()  # Highest at top

    # Step 4: Save chart
    plt.tight_layout()
    plt.savefig(f"E:\\python programs\\__00AQI dashboard\\reports\\summary_charts\\top_cities.png", dpi=300)
    plt.show()

    print(f"✅ Chart saved as 'reports/summary_charts/top_cities.png'")

if __name__ == "__main__":
    file_path = f"Data\\air_quality_data.csv"
    df = clean_data(file_path)
    plot_top_cities(df)
