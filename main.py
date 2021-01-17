import requests
import pandas as pd

date_string = '2021-01-12'
symbols = ['DELL', 'CRM']

access_key = 'e6bb32ac5f262fa52af11b7abcf170eb'
response =requests.get('http://api.marketstack.com/v1/eod/' + date_string + '?access_key=' + access_key + '&symbols=' + ','.join(symbols))
stocks_data = response.json()

col1 = []
col2 = []
col3 = []
col4 = []

for stock_data in stocks_data['data']:
    col1.append(stock_data['symbol'])
    col2.append(stock_data['date'][0:10])
    col3.append(stock_data['close'])
    col4.append(stock_data['adj_close'])

d = {'Symbol': col1, 'Close Date': col2, 'Close Price': col3, 'Adjusted Close Price': col4}

df_result = pd.DataFrame(data=d)

print(df_result)

df_result.to_excel ('result.xlsx', index = False, header=True)