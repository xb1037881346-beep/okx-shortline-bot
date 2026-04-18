import time
import random

class OrderExecution:
    def __init__(self):
        self.positions = {}

    def create_order(self, symbol, qty, side):
        # Simulate order creation
        print(f'Creating order: {side} {qty} of {symbol}')
        # Randomly determine if order is successful or fails
        if random.choice([True, False]):
            order_id = random.randint(1000, 9999)
            print(f'Order created successfully: {order_id}')
            return order_id
        else:
            raise Exception('Order creation failed')

    def confirm_order(self, order_id):
        # Simulate order confirmation
        print(f'Confirming order: {order_id}')
        time.sleep(1)
        print(f'Order {order_id} confirmed.')

    def check_position(self, symbol):
        # Simulating checking positions
        if symbol in self.positions:
            print(f'Position for {symbol}: {self.positions[symbol]}')
        else:
            print(f'No position for {symbol}')

    def execute(self, symbol, qty, side):
        try:
            # Create order
            order_id = self.create_order(symbol, qty, side)
            # Confirm order
            self.confirm_order(order_id)
            # Update positions
            if side == 'buy':
                self.positions[symbol] = self.positions.get(symbol, 0) + qty
            elif side == 'sell':
                self.positions[symbol] = self.positions.get(symbol, 0) - qty
            print(f'Current positions: {self.positions}')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    order_exec = OrderExecution()
    order_exec.execute('BTCUSDT', 1, 'buy')  # Example order
