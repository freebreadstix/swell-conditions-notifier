import calendar
from datetime import datetime, timedelta
import pandas as pd
import requests

def get_tide(station=9413450, num_days=3):
    product, datum, time_zone, units = "predictions", "MLLW", "lst_ldt", "english"
    data_format = "json"

    now = datetime.now()

    begin_date = now.strftime('%Y%m%d')
    end_date = (now + timedelta(days=num_days)).strftime('%Y%m%d')

    url = f'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={begin_date}&end_date={end_date}&station={station}&product=predictions&datum=MLLW&time_zone=lst_ldt&units=english&format={data_format}'

    response = requests.get(url).json()
    predictions = response['predictions']

    '''
    TODO: 
    - get sunrise/first light, sunset
    - return times as formatted list
    - return high, low tide
    Wednesday
    10:45 | 2.5
    15:00 | 5
    18:00 | -0.3

    10:45 || 2.5
    15:00 || 5
    18:00 || -0.3

    [10:45] [2.5]
    [15:00] [5]
    [18:00] [-0.3]

    [22:00, 0.273
    23:00, 1.162
    00:00, 2.099]
    '''
    df = pd.DataFrame(predictions)

    # Get data by hour
    df = df.iloc[::10]

    df['dt_object'] = df['t'].apply(lambda x: pd.to_datetime(x).to_pydatetime())
    df['day'] = df['dt_object'].apply(lambda x: calendar.day_name[x.weekday()])
    df['time'] = df['dt_object'].apply(lambda x: x.strftime("%H:%M"))

    sunrise, sunset = "05:00", "20:00"
    df = df[(df['time'] >= sunrise) & (df['time'] <= sunset)]

    # Filter by ideal tide period
    df['v'] = df['v'].astype('float')
    df = df[df['v'] < 3.5]

    return df[['day', 'time', 'v']]

if __name__ == "__main__":
    station = 9413450 # Monterey
    num_days = 3
    df = get_tide(station, num_days)
    print(df)
