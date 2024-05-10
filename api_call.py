import requests
import numpy as np

def fetch_co2_data():
    url = "http://api.worldbank.org/v2/country/BR/indicator/EN.ATM.CO2E.PC?format=json&date=2017:2020"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_co2_data(data):
    if not data:
        print("No data to process.")
        return
    
    emissions_records = []
    try:
        emissions_data = data[1] 
        for record in emissions_data:
            year = int(record['date'])
            co2_per_capita = record['value']
            if co2_per_capita is not None:
                emissions_records.append((year, f"{co2_per_capita:.4f} CO2 Emissions (metric tons per capita)"))
            else:
                emissions_records.append((year, "Data not available"))
    except Exception as e:
        print(f"Error processing data: {e}")

    return emissions_records

def predict_future_emissions(years, emissions):    # Fit a linear model
    coefficients = np.polyfit(years, emissions, 1)
    model = np.poly1d(coefficients)


    predicted_years = np.array([2021, 2022, 2023, 2024, 2025, 2026])
    predicted_emissions = model(predicted_years)

    future_emissions = []
    for year, emission in zip(predicted_years, predicted_emissions):
        future_emissions.append((year, f"{emission:.4f} Predicted CO2 Emissions (metric tons per capita)"))

    return future_emissions

def main():
    data = fetch_co2_data()
    historical_emissions = process_co2_data(data)
    if historical_emissions:
        # Data from the user input
        years = np.array([record[0] for record in historical_emissions if "Data not available" not in record[1]])
        emissions = np.array([float(record[1].split()[0]) for record in historical_emissions if "Data not available" not in record[1]])

        future_emissions = predict_future_emissions(years, emissions)

        # Combine and sort emissions records
        all_emissions = historical_emissions + future_emissions
        all_emissions.sort()  # Sort by year

        for year, emission in all_emissions:
            print(f"{year}: {emission}")

if __name__ == "__main__":
    main()
