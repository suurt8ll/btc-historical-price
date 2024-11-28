import pandas as pd
import matplotlib.pyplot as plt

def plot_bitcoin_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path, parse_dates=['Date'])
    
    # Plot the data on a logarithmic y scale
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Bitcoin Closing Price', color='orange')
    
    # Set the y-axis to a logarithmic scale
    plt.yscale('log')
    
    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title('Bitcoin Closing Prices (Log Scale)')
    
    # Add a legend
    plt.legend()
    
    # Add grid lines
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Display the plot
    plt.tight_layout()
    plt.show()

# Define the file path
file_path = 'bitcoin_daily_prices.csv'

# Plot the data
plot_bitcoin_data(file_path)
