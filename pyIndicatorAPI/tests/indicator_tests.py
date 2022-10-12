import time

from ..indicators import Client

api = ''


class TestClient:

    def test_rsi(self):
        client = Client(api)
        response = client.rsi('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_stochastic_rsi(self):
        client = Client(api)
        response = client.stochastic_rsi('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_macd(self):
        client = Client(api)
        response = client.macd('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_adx(self):
        client = Client(api)
        response = client.adx('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_atr(self):
        client = Client(api)
        response = client.adx('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_awesome_oscillator(self):
        client = Client(api)
        response = client.awesome_oscillator('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_bollinger_bands(self):
        client = Client(api)
        response = client.bollinger_bands('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_cci(self):
        client = Client(api)
        response = client.cci('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_force_index(self):
        client = Client(api)
        response = client.force_index('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_kst(self):
        client = Client(api)
        response = client.kst('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_money_flow_index(self):
        client = Client(api)
        response = client.money_flow_index('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_on_balance_volume(self):
        client = Client(api)
        response = client.on_balance_volume('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_parabolic_stop_and_reverse(self):
        client = Client(api)
        response = client.parabolic_stop_and_reverse('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_sma(self):
        client = Client(api)
        response = client.sma('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_stochastic_oscillator(self):
        client = Client(api)
        response = client.stochastic_oscillator('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_trix(self):
        client = Client(api)
        response = client.trix('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_volume_profile(self):
        client = Client(api)
        response = client.volume_profile('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_ema(self):
        client = Client(api)
        response = client.ema('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_wma(self):
        client = Client(api)
        response = client.wma('BTC/USDT')
        time.sleep(2)
        assert response is not None
        
    def test_wema(self):
        client = Client(api)
        response = client.wema('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_williams_r(self):
        client = Client(api)
        response = client.williams_r('BTC/USDT')
        time.sleep(2)
        assert response is not None

    def test_ichimoku_cloud(self):
        client = Client(api)
        response = client.ichimoku_cloud('BTC/USDT')
        time.sleep(2)
        assert response is not None
