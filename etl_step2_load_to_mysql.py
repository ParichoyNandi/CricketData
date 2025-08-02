import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSVs
matches_df = pd.read_csv("clean_matches.csv")
deliveries_df = pd.read_csv("clean_deliveries.csv")

# Rename 'over' column to avoid SQL keyword conflict
deliveries_df.rename(columns={'over': 'over_number'}, inplace=True)

# MySQL connection
user = 'root'
password = '6297'
host = 'localhost'
database = 'cricket_etl'

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Load to MySQL
matches_df.to_sql('matches', con=engine, if_exists='replace', index=False)
deliveries_df.to_sql('deliveries', con=engine, if_exists='replace', index=False)

print("Data loaded into MySQL successfully.")
