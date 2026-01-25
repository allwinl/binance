# config.py   ── must be named exactly config.py

API_KEY = 'swNCkZLoqzFnYPreUDrFAAnoAxsx16PcJSDlU3AEpep7MwaOCVXzq3YHUDJkZvu8'
API_SECRET = 'f7774SEvatAbZJHNP6NYZu6dtAb6zxYUBmxQp6c8d90PbNvlvKLYl1ofF7A1J4qn'


SYMBOL               = "XRPUSDT"
INTERVAL             = "15m"
EMA_PERIOD           = 21
LEVERAGE             = 3               # keep low
POSITION_PCT         = 0.01            # 1% of available USDT per trade – very conservative
DAILY_OPEN_TOLERANCE = 0.003
MIN_SAFE_BALANCE     = 30.0

SLEEP_SECONDS        = 3600 + 30       # ~once per hour
