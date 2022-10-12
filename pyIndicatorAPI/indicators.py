import requests

from handlers.inderrhandler import handle_status_code, handle_log

# The way of using this class is simple
# Create instance of an object class
# The object is bound to one market pair e.g. BTC/USDT
# Happily read the indicators!
# Big win =]
class Client:
    def __init__(self, api_key, create_logs=False):
        self.create_logs = create_logs
        self.headers = {
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': 'crypto-indicators-rest.p.rapidapi.com'
        }
        # This api seems to work well.
        # There are plenty of indicators,
        # Which may be helpful to users.
        # Limit - 2000 requests per month for free.
        # I will add all available indicators ASAP.
        self.url = 'https://crypto-indicators-rest.p.rapidapi.com/'

    def rsi(self, market, timeframe='1d', period=14):
        url = self.url + 'rsi'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def stochastic_rsi(self,
                       market,
                       timeframe='1d',
                       rsiperiod=14,
                       stochasticperiod=14,
                       kperiod=3,
                       dperiod=3):
        url = self.url + 'stochasticrsi'
        data = {
            'market': market,
            'timeframe': timeframe,
            'rsiPeriod': rsiperiod,
            'stochasticPeriod': stochasticperiod,
            'kPeriod': kperiod,
            'dPeriod': dperiod
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def macd(self,
             market,
             timeframe='1d',
             fastperiod=12,
             slowperiod=26,
             signalperiod=9,
             simplemaoscillator=False,
             simplemasignal=False):
        url = self.url + 'macd'
        data = {
            'market': market,
            'timeframe': timeframe,
            'fastPeriod': fastperiod,
            'slowPeriod': slowperiod,
            'signalPeriod': signalperiod,
            'SimpleMAOscillator': simplemaoscillator,
            'SimpleMASignal': simplemasignal
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def adx(self, market, timeframe='1d', period=14):
        url = self.url + 'adx'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def atr(self, market, timeframe='1d', period=14):
        url = self.url + 'atr'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def awesome_oscillator(self, market, timeframe='1d', fastperiod=5, slowperiod=34):
        url = self.url + 'awesomeOscillator'
        data = {
            'market': market,
            'timeframe': timeframe,
            'fastPeriod': fastperiod,
            'slowPeriod': slowperiod
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def bollinger_bands(self, market, timeframe='1d', period=14):
        url = self.url + 'bollingerBands'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def cci(self, market, timeframe='1d', period=20):
        url = self.url + 'cci'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def force_index(self, market, timeframe='1d', period=1):
        url = self.url + 'forceIndex'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def kst(self,
            market,
            timeframe='1d',
            rocper1=10,
            rocper2=15,
            rocper3=20,
            rocper4=30,
            smarocper1=10,
            smarocper2=10,
            smarocper3=10,
            smarocper4=15,
            signalperiod=9):
        url = self.url + 'kst'
        data = {
            'market': market,
            'timeframe': timeframe,
            'ROCPer1': rocper1,
            'ROCPer2': rocper2,
            'ROCPer3': rocper3,
            'ROCPer4': rocper4,
            'SMAROCPer1': smarocper1,
            'SMAROCPer2': smarocper2,
            'SMAROCPer3': smarocper3,
            'SMAROCPer4': smarocper4,
            'signalPeriod': signalperiod
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def money_flow_index(self, market, timeframe='1d', period=14):
        url = self.url + 'moneyFlowIndex'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def on_balance_volume(self, market, timeframe='1d'):
        url = self.url + 'onBalanceVolume'
        data = {
            'market': market,
            'timeframe': timeframe
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def parabolic_stop_and_reverse(self, market, timeframe='1d', step=0.2, max_=0.2):
        url = self.url + 'psar'
        data = {
            'market': market,
            'timeframe': timeframe,
            'step': step,
            'max': max_
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            handle_status_code(response)
            return None

    def sma(self, market, timeframe='1d', period=9):
        url = self.url + 'sma'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def stochastic_oscillator(self, market, timeframe='1d', period=14, signalperiod=3):
        url = self.url + 'stochasticOscillator'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period,
            'signalPeriod': signalperiod
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def trix(self, market, timeframe='1d', period=18):
        url = self.url + 'trix'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def volume_profile(self, market, timeframe='1d', nofbars=14):
        url = self.url + 'volumeProfile'
        data = {
            'market': market,
            'timeframe': timeframe,
            'noOfBars': nofbars
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def ema(self, market, timeframe='1d', period=9):
        url = self.url + 'ema'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def wma(self, market, timeframe='1d', period=9):
        url = self.url + 'wma'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def wema(self, market, timeframe='1d', period=7):
        url = self.url + 'wema'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def williams_r(self, market, timeframe='1d', period=14):
        url = self.url + 'williamsR'
        data = {
            'market': market,
            'timeframe': timeframe,
            'period': period
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None

    def ichimoku_cloud(self,
                       market,
                       timeframe='1d',
                       conversionperiod=9,
                       baseperiod=26,
                       spanperiod=52,
                       displacement=26):
        url = self.url + 'ichimokuCloud'
        data = {
            'market': market,
            'timeframe': timeframe,
            'conversionPeriod': conversionperiod,
            'basePeriod': baseperiod,
            'spanPeriod': spanperiod,
            'displacement': displacement
        }
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            return response.json()
        else:
            if self.create_logs:
                handle_status_code(response)
            return None


if __name__ == '__main__':
    pass

