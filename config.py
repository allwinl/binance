# config.py   ── must be named exactly config.py

API_KEY = 'swNCkZLoqzFnYPreUDrFAAnoAxsx16PcJSDlU3AEpep7MwaOCVXzq3YHUDJkZvu8'


SYMBOL               = "BTCUSDT"
INTERVAL             = "1h"
EMA_PERIOD           = 21
LEVERAGE             = 5
POSITION_PCT         = 0.03
DAILY_OPEN_TOLERANCE = 0.003
MIN_SAFE_BALANCE     = 50.0

RUN_LIVE             = False
BASE_URL             = "https://testnet.binancefuture.com"   # or None for real money

# This is the line that's missing or misspelled in your file
SLEEP_SECONDS        = 3600 + 20          # ~1 hour + buffer
