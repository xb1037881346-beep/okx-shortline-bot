class StateMachine:
    def __init__(self):
        self.state = 'FLAT'

    def set_state(self, state):
        if state in ['FLAT', 'LONG', 'SHORT']:
            self.state = state
            print(f'State changed to: {self.state}')
        else:
            print('Invalid state!')

    def get_state(self):
        return self.state

    def on_event(self, event):
        if event == 'buy':
            self.set_state('LONG')
        elif event == 'sell':
            self.set_state('SHORT')
        elif event == 'hold':
            self.set_state('FLAT')
        else:
            print('Unknown event!')
