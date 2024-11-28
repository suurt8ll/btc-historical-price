import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_bitcoin_daily_data(ticker, start_date, end_date):
    # Fetch the data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Return only the 'Close' column
    return data['Close']

def get_latest_date_from_csv(file_path):
    try:
        # Read the existing CSV file
        df = pd.read_csv(file_path, parse_dates=['Date'])
        # Get the latest date
        latest_date = df['Date'].max()
        return latest_date
    except FileNotFoundError:
        # If the file does not exist, return None
        return None

def main():
    # Define the ticker symbol for Bitcoin
    ticker = "BTC-USD"
    
    # Define the file path
    file_path = 'bitcoin_daily_prices.csv'
    
    # Get the latest date from the existing CSV file
    latest_date = get_latest_date_from_csv(file_path)
    
    if latest_date is not None:
        # Convert to string format for display
        latest_date_str = latest_date.strftime('%Y-%m-%d')
        print(f"The latest date in the file is: {latest_date_str}")
        start_date = latest_date + timedelta(days=1)
        start_date_str = start_date.strftime('%Y-%m-%d')
    else:
        print("No existing data found.")
        # Prompt the user for the start date
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    
    # Get the current date as the default end date
    current_date = datetime.now().strftime('%Y-%m-%d')
    end_date_input = input(f"Enter the end date (YYYY-MM-DD, press Enter for {current_date}): ")
    
    # Use the current date if the user presses Enter
    end_date = datetime.strptime(end_date_input, '%Y-%m-%d') if end_date_input else datetime.strptime(current_date, '%Y-%m-%d')
    
    # Fetch the daily data
    daily_data = fetch_bitcoin_daily_data(ticker, start_date, end_date)
    
    # Convert the index to a DataFrame and rename the column
    df = daily_data.reset_index()
    df.columns = ['Date', 'Close']
    
    # If there is existing data, remove the duplicate entry if it exists
    if latest_date is not None:
        df = df[df['Date'] > latest_date]
    
    # Append the new data to the existing CSV file or create a new one if it doesn't exist
    if latest_date is not None:
        # Append the new data
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # Create a new file
        df.to_csv(file_path, index=False)
    
    print(f"Data from {start_date_str} to {end_date.strftime('%Y-%m-%d')} has been saved to {file_path}")

if __name__ == "__main__":
    main()
