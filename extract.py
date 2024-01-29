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
df.to_csv('new_df.csv', index=False)