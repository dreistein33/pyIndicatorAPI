# pyIndicatorAPI
IndicatorAPI.com wrapper

How to install:
1) Make sure you have latest version of pip
2) Type `pip install pyIndicatorAPI` in the terminal

Usage:
```python
from pyIndicatorAPI.indicators import Client

client = Client(YOUR_API_KEY)
rsi_values = client.rsi('BTC/USDT')
```
