import ccxt
import pandas as pd
from datetime import datetime, timedelta

exchange = ccxt.binance()


symbols = symbols = [
    'BTC/USDT',
    'ETH/USDT',
    'BNB/USDT',
    'XRP/USDT',
    'ADA/USDT',
    'SOL/USDT',
    'DOT/USDT',
    'DOGE/USDT',
    'SHIB/USDT',
    'MATIC/USDT',
    'LINK/USDT',
    'TRX/USDT',
    'LTC/USDT',
    'BCH/USDT',
    'AVAX/USDT',
    'UNI/USDT',
    'XLM/USDT',
    'FTM/USDT',
    'ALGO/USDT',
    'FIL/USDT',
    'VET/USDT',
    'ICP/USDT',
    'ETC/USDT',
    'AAVE/USDT',
    'THETA/USDT',
    'XMR/USDT',
    'CRV/USDT',
    'SAND/USDT',
    'EOS/USDT',
    'ZEC/USDT'
]


timeframe = '1d'

def fetch_max_daily_data(symbol):
    all_data = []
    since = exchange.parse8601('2015-08-01T00:00:00Z')  # Start date for data collection

    while True:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=1000)
        if not ohlcv:
            break

        all_data.extend(ohlcv)
        since = ohlcv[-1][0] + 24 * 60 * 60 * 1000  # +1 day in milliseconds

    return all_data

for symbol in symbols:
    data = fetch_max_daily_data(symbol)

    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    df.set_index('timestamp', inplace=True)

    name = symbol.split('/')[0]
    dataset = df.to_csv(f"{name} dataset.csv")
    print(f"{name} done!")