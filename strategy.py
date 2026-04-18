class StrategyAnalyzer:
    def __init__(self, data):
        self.data = data

    def compute_ema(self, period):
        return self.data['Close'].ewm(span=period, adjust=False).mean()

    def generate_signals(self):
        # Calculate EMA20 and EMA50
        self.data['EMA20'] = self.compute_ema(20)
        self.data['EMA50'] = self.compute_ema(50)

        # Generate signals
        self.data['Signal'] = 0
        self.data['Signal'][20:] = \
            (self.data['EMA20'][20:] > self.data['EMA50'][20:]).astype(int)
        self.data['Position'] = self.data['Signal'].diff()

        # Apply volume confirmation
        self.data['Buy'] = (self.data['Position'] == 1) & (self.data['Volume'] > self.data['Volume'].rolling(window=20).mean())
        self.data['Sell'] = (self.data['Position'] == -1) & (self.data['Volume'] > self.data['Volume'].rolling(window=20).mean())
        self.data['Hold'] = (self.data['Buy'] == False) & (self.data['Sell'] == False)

    def get_signals(self):
        return self.data[['Date', 'Close', 'EMA20', 'EMA50', 'Buy', 'Sell', 'Hold']]
