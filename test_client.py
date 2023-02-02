import unittest
import client;


class ClientTest(unittest.TestCase):
    

    def test_get_ratio_between_two_prices(self):
        return_value = client.getRatio(120, 50)
        expected_value = 2.4
        self.assertEqual(expected_value, return_value)
    

    def test_get_ratio_price_b_is_zero(self):
        return_value = client.getRatio(113, 0)
        expected_value = None
        self.assertEqual(expected_value, return_value)

    
if __name__=="__main__":
    unittest.main()