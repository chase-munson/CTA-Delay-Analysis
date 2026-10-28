# Import libraries
import pandas as pd
import sqlite3

# Define the path to the SQLite database
data_path = '../data/cta_data_05_2026.db'

# Connect to the SQLite database and read the train_data table into a DataFrame
with sqlite3.connect(data_path) as conn:
    df = pd.read_sql('SELECT * FROM train_data', conn)

# Clean up the 'line' column by replacing abbreviations with full line names
df['line'] = df['line'].replace({
    'Brn': 'Brown',
    'G': 'Green',
    'Org': 'Orange',
    'P': 'Purple',
    'Y': 'Yellow',
})

# Convert the 'timestamp' column to datetime format with UTC timezone
df['timestamp'] = pd.to_datetime(
    df['timestamp'],
    format='ISO8601',
    utc=True
)

# Convert the 'predicted_time' column to datetime format with UTC timezone
df['predicted_time'] = pd.to_datetime(
    df['predicted_time'],
    format='ISO8601',
    utc=True
)

# Convert the 'arrival_time' column to datetime format with UTC timezone
df['arrival_time'] = pd.to_datetime(
    df['arrival_time'],
    format='ISO8601',
    utc=True
)