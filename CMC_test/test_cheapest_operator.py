import unittest
from cheapest_operator import OperatorPriceList, find_cheapest_operator

class TestOperatorPriceList(unittest.TestCase):

    def setUp(self):
        # Thiết lập dữ liệu mẫu cho các nhà cung cấp
        self.operators = [
            OperatorPriceList("Operator A", {
                "1": 0.9,
                "268": 5.1,
                "46": 0.17,
                "4620": 0.0,
                "468": 0.15,
                "4631": 0.15,
                "4673": 0.9,
                "46732": 1.1
            }),
            OperatorPriceList("Operator B", {
                "1": 0.92,
                "44": 0.5,
                "46": 0.2,
                "467": 1.0,
                "48": 1.2
            }),
        ]

    def test_find_cheapest_operator(self):
        # Test case 1: Số điện thoại với tiền tố "46732"
        phone_number = "4673212345"
        operator, price = find_cheapest_operator(phone_number, self.operators)
        print(f"Test case 1: Phone number : {phone_number} Operator : {operator}, Price : {price}/phút")

        # Test case 2: Số điện thoại với tiền tố "46"
        phone_number = "4681234567"
        operator, price = find_cheapest_operator(phone_number, self.operators)
        print(f"Test case 2: Phone number : {phone_number} Operator : {operator}, Price : {price}/phút")

        # Test case 3: Số điện thoại không có tiền tố phù hợp
        phone_number = "999123456"
        operator, price = find_cheapest_operator(phone_number, self.operators)
        print(f"Test case 3: Phone number : {phone_number} Operator : {operator}, Price : {price}/phút")

if __name__ == "__main__":
    unittest.main()