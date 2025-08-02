import pandas as pd

# Load CSV files
matches_df = pd.read_csv("matches.csv")
deliveries_df = pd.read_csv("deliveries.csv")

# Preview top rows
print("Matches Data:")
print(matches_df.head())

print("\nDeliveries Data:")
print(deliveries_df.head())

# Check for nulls
print("\nMissing values in Matches:")
print(matches_df.isnull().sum())

print("\nMissing values in Deliveries:")
print(deliveries_df.isnull().sum())

# Clean column names (optional: lowercase and remove spaces)
matches_df.columns = matches_df.columns.str.strip().str.lower()
deliveries_df.columns = deliveries_df.columns.str.strip().str.lower()

# Convert date column to datetime
matches_df['date'] = pd.to_datetime(matches_df['date'])

# Fill null values where necessary
matches_df['winner'] = matches_df['winner'].fillna("No Result")
deliveries_df['player_dismissed'] = deliveries_df['player_dismissed'].fillna("Not Out")
deliveries_df['dismissal_kind'] = deliveries_df['dismissal_kind'].fillna("None")

# Save cleaned copies (optional for next steps)
matches_df.to_csv("clean_matches.csv", index=False)
deliveries_df.to_csv("clean_deliveries.csv", index=False)

print("\nData cleaned and saved.")
