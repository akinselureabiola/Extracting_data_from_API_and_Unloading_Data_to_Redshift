import requests
import json
import pandas as pd

url = "http://universities.hipolabs.com/search?country=United+States"
response = requests.get(url)
data = response.text

# converting string to JSON
parsed = json.loads(data)
json_data = print(json.dumps(parsed))
new_df = pd.DataFrame({'col':parsed})

# Convert DataFrame to Csv file format
df_csv = df.to_csv('../test/uni.csv', index=False)

#Convert CSV file to Paquet file format
df_paquet = df.to_parquet('../test/uni.parquet', index=False)