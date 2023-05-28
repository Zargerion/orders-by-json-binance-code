from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json
import random

api = "Your API Key"
secret = "Your API Secret"

try:
    client = Client(api, secret, testnet=True)
except Exception as e:
    print("Cannot make client", e)

class Utils:
    def average_volume_maker(volume: float, number: float) -> float:
        try:
            avg_volume = volume / number
            print(f'Average volume: {avg_volume}')
            return avg_volume
        except Exception as e:
            print('Cannot get average volume', e)
            return

    def random_prices_maker(priceMin: float, priceMax: float, number: float) -> dict:
        try:
            random_prices = [random.uniform(priceMin, priceMax) for i in range(number)]
            print(f'Average prices: {random_prices}')
            return random_prices
        except Exception as e:
            print('Cannot get random prices', e)
            return

    def random_volume_maker(volume: float, amountDif: float) -> float:
        '''It makes random volume'''
        try:
            min_vol = volume - amountDif
            max_vol = volume + amountDif
            volume = random.uniform(min_vol, max_vol)
            return round(volume, 1)
        except Exception as e:
            print('Problem with function rand_vol()', e)
            return

class OrderMaker:
    def __init__(self, client: Client):
        self.client = client
        self.volume = 0.0
        self.number = 0.0
        self.amountDif = 0.0
        self.side = ''
        self.priceMin = 0.0
        self.priceMax = 0.0
        self.order_list = []
        self.avg_volume = 0.0
        self.random_prices_list = []

    def get_json(self, json_file: str):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            data

            self.volume = data['volume']
            self.number = data['number']
            self.amountDif = data['amountDif']
            self.side = data['side']
            self.priceMin = data['priceMin']
            self.priceMax = data['priceMax']
            self.avg_volume = Utils.average_volume_maker(self.volume, self.number)
            self.random_prices_list = Utils.random_prices_maker(self.priceMin, self.priceMax, self.number)

            print(f'Volume: {self.volume}')
            print(f'Number: {self.number}')
            print(f'Amount Difference: {self.amountDif}')
            print(f'Side: {self.side}')
            print(f'Minimum Price: {self.priceMin}')
            print(f'Maximum Price: {self.priceMax}')
            print(f'Average volume: {self.avg_volume}')
        except Exception as e:
            print('Cannot read json', e)

    def get_balance(self):
        try:
            self.balance = self.client.futures_account_balance()[3]['balance']
            print("balance in usdt =", self.balance)
        except Exception as e:
            print("Cannot get balance", e)

    def make_orders(self):
        try:
            for i in range(self.number):

                usdt_volume = Utils.random_volume_maker(self.avg_volume, self.amountDif)
                BNB_PRICE = client.futures_mark_price(symbol='BNBUSDT')['markPrice']
                quantity = round(usdt_volume / float(BNB_PRICE), 1)

                order = client.futures_create_order(
                    symbol='BNBUSDT',
                    side=self.side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=round(self.random_prices_list[i], 3),
                    reduceOnly=False,
                    newOrderRespType='RESULT'
                )

                self.order_list.append(order)
        except Exception as e:
                print('Cannot make orders', e)
        
    def cancel_orders(self):
        try:
            for order in self.order_list:
                result = client.futures_cancel_order(
                    symbol=order['symbol'],
                    orderId=order['orderId']
                )
                print(result)
        except Exception as e:
                print('Cannot cancel orders', e)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == "__main__":

    om = OrderMaker(client=client)
    om.get_balance()
    om.get_json('data.json')
    om.make_orders()
    import time 
    time.sleep(10)
    om.cancel_orders()