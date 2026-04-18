class RiskManager:
    def __init__(self, account_balance, risk_per_trade):
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade
        self.stop_loss_level = None
        self.take_profit_level = None
        self.daily_loss_limit = None
        self.loss_streak = 0
        self.current_daily_loss = 0

    def calculate_position_size(self):
        """Calculate the position size based on risk per trade."""
        return self.account_balance * self.risk_per_trade

    def set_stop_loss(self, entry_price, stop_loss_percentage):
        """Set the stop loss level based on entry price and percentage."""
        self.stop_loss_level = entry_price * (1 - stop_loss_percentage)

    def set_take_profit(self, entry_price, take_profit_percentage):
        """Set the take profit level based on entry price and percentage."""
        self.take_profit_level = entry_price * (1 + take_profit_percentage)

    def set_daily_loss_limit(self, limit):
        """Set a daily loss limit."""
        self.daily_loss_limit = limit

    def record_loss(self, amount):
        """Record a loss and check for loss streaks."""
        self.current_daily_loss += amount
        if self.current_daily_loss >= self.daily_loss_limit:
            self.reset_daily_loss()
        if amount > 0:  # Assuming amount is positive for a loss
            self.loss_streak += 1

    def reset_daily_loss(self):
        """Reset the daily loss tracker."""
        self.current_daily_loss = 0

    def reset_loss_streak(self):
        """Reset the loss streak counter."""
        self.loss_streak = 0
