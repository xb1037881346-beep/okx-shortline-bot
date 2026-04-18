import ccxt
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataFetcher:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange = self.initialize_exchange()

    def initialize_exchange(self):
        if self.exchange_name == 'binance':
            return ccxt.binance()
        elif self.exchange_name == 'kraken':
            return ccxt.kraken()
        else:
            raise ValueError('Exchange not supported')

    def fetch_ohlcv(self, symbol, timeframe='1m', limit=100):
        return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    def fetch_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)

    def fetch_balance(self):
        return self.exchange.fetch_balance()

    def fetch_positions(self):
        return self.exchange.fetch_positions()