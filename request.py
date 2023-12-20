from datetime import datetime, timedelta
import pandas as pd
import requests

station = 9413450 # Monterey

product, datum, time_zone, units = "predictions", "MLLW", "lst_ldt", "english"
data_format = "json"

now = datetime.now()
num_days = 3

begin_date = now.strftime('%Y%m%d')
end_date = (now + timedelta(days=num_days)).strftime('%Y%m%d')

sample_url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20231117&end_date=20231119&station=9413450&product=predictions&datum=MLLW&time_zone=lst_ldt&units=english&format=json'
url = ''

response = requests.get(sample_url).json()
predictions = response['predictions']


# TODO: try csv, add check to verify complete csv, time both

'''
TODO: 
- get sunrise/first light, sunset
- convert str, filter by sunrise etc
- convert time to day?, separate day, time
- return times as list?
Wednesday
[22:00, 0.273
23:00, 1.162
00:00, 2.099]
'''
df = pd.DataFrame(predictions)
df = df.iloc[::10]
df['v'] = df['v'].astype('float')
df = df[df['v'] < 3.5]

df = df.iloc[10:50]
print(df)

print(begin_date, end_date)
