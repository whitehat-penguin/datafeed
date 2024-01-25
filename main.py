from tvDatafeed import TvDatafeed, Interval
import pandas as pd

username = 'longndm508i'
password = '_W2PqwN.Bfs2'

tv = TvDatafeed(username, password)

csv_file_path = '/Users/luigi/TVdata/data_year.csv'

index_data = tv.get_hist(symbol='BTCUSDT',exchange='BINANCE',interval=Interval.in_5_minute,n_bars=10000)


index_data_reset = index_data.reset_index()
index_data_reset.to_csv(csv_file_path, index=False)


# print(index_data)