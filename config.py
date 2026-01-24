# config.py
# NEVER commit this file anywhere public

API_KEY    = "your_actual_api_key_here"
API_SECRET = "your_actual_api_secret_here"

# Trading settings
SYMBOL              = "BTCUSDT"
INTERVAL            = "1h"
EMA_PERIOD          = 21
LEVERAGE            = 5
POSITION_PCT        = 0.03           # 3% of available USDT
DAILY_OPEN_TOLERANCE = 0.003
MIN_SAFE_BALANCE    = 50.0

# Very important – control live vs simulation
RUN_LIVE            = False          # Change to True ONLY after full testing

# URL – use testnet until you're 100% sure
BASE_URL            = "https://testnet.binancefuture.com"   # ← safe choice for now
# For real money (after testing): BASE_URL = None
