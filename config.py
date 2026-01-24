

API_KEY = 'swNCkZLoqzFnYPreUDrFAAnoAxsx16PcJSDlU3AEpep7MwaOCVXzq3YHUDJkZvu8'
API_SECRET = 'f7774SEvatAbZJHNP6NYZu6dtAb6zxYUBmxQp6c8d90PbNvlvKLYl1ofF7A1J4qn'


SYMBOL           = "BTCUSDT"
INTERVAL         = "1h"
EMA_PERIOD       = 21
LEVERAGE         = 5
POSITION_PCT     = 0.03          # 3% of available balance per trade
DAILY_OPEN_TOLERANCE = 0.003     # 0.3%
MIN_SAFE_BALANCE = 50.0          # emergency close if balance drops below

RUN_LIVE     = True              # False = dry run (print only, no orders)
SLEEP_SECONDS = 3600 + 15        # roughly once per hour

