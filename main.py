from scripts.process_data import clean_data, city_wise_summary
from scripts.visualize_data import plot_top_cities
# from scripts.trend_analysis import city_pollution_trend
# from scripts.multi_city_trend import multi_city_trend

def main():
    """Main pipeline for Air Quality Data Analysis"""
    file_path = f"E:\\python programs\\__00AQI dashboard\\Data\\air_quality_data.csv"

    print("🚀 Starting Air Quality Data Analysis...\n")

    # Step 1: Load and clean data
    df = clean_data(file_path)
    print("✅ Data loaded and cleaned successfully.")

    # Step 2: City-wise summary
    print("\n📊 Generating city-wise summary...")
    city_wise_summary(df)

    # Step 3: Visualize top polluted cities
    print("\n📈 Creating Top 10 Cities pollution chart...")
    plot_top_cities(df)

    # Step 4: Visualize trend for a single city (change name as needed)
    # print("\n🌆 Plotting pollution trend for Gaya...")
    # city_pollution_trend(df, "Gaya")

    # Step 5: Visualize multi-city comparison
    # print("\n🌍 Plotting multi-city trend comparison...")
    # cities_to_compare = ["Gaya", "Patna", "Buxar", "Chhapra"]
    # multi_city_trend(df, cities_to_compare)

    # print("\n🎯 All visualizations generated successfully!")
    # print("Check the 'reports/summary_charts' folder for output images.")

if __name__ == "__main__":
    main()
