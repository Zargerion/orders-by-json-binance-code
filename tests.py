from main import *
import unittest
import time

class TestOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.om = OrderMaker(client=client)

    def test_cancel_orders(self):
        self.om.get_json('data.json')
        self.om.cancel_orders()
        orders = client.futures_get_open_orders(symbol='BNBUSDT')
        time.sleep(1)
        print('Open orders:', len(orders))
        count = len(orders)
        self.assertIs(count, 0)

    def test_make_orders(self):
        self.om.get_json('data.json')
        self.om.make_orders()
        orders = client.futures_get_open_orders(symbol='BNBUSDT')
        time.sleep(1)
        print('Open orders:', len(orders))
        count = len(orders)
        self.assertIs(count, 5)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOrders('test_make_orders'))
    suite.addTest(TestOrders('test_cancel_orders'))
    unittest.TextTestRunner().run(suite)
