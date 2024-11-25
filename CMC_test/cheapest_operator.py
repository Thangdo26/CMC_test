class OperatorPriceList:
    def __init__(self, name, price_list):
        """
        :param name: Tên của nhà cung cấp
        :param price_list: Dictionary chứa prefix và giá cước
        """
        self.name = name
        self.price_list = price_list

    def get_price(self, phone_number):
        """
        Lấy giá cước cho một số điện thoại cụ thể.
        :param phone_number: Số điện thoại cần kiểm tra
        :return: Giá cước (hoặc None nếu không có prefix phù hợp)
        """
        longest_prefix = ""
        price = None
        for prefix in self.price_list:
            if phone_number.startswith(prefix):
                if len(prefix) > len(longest_prefix):
                    longest_prefix = prefix
                    price = self.price_list[prefix]
        return price


def find_cheapest_operator(phone_number, operators):
    """
    Tìm nhà cung cấp rẻ nhất cho một số điện thoại.
    :param phone_number: Số điện thoại cần kiểm tra
    :param operators: Danh sách các đối tượng OperatorPriceList
    :return: Tên nhà cung cấp rẻ nhất và giá cước (hoặc None nếu không nhà cung cấp nào phù hợp)
    """
    cheapest_price = float('inf')
    cheapest_operator = None

    for operator in operators:
        price = operator.get_price(phone_number)
        if price is not None and price < cheapest_price:
            cheapest_price = price
            cheapest_operator = operator.name

    return cheapest_operator, cheapest_price if cheapest_operator else None


if __name__ == "__main__":
    # Dữ liệu mẫu
    operators = [
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

    # Số điện thoại cần kiểm tra
    phone_number = "4673212345"

    # Tìm nhà cung cấp rẻ nhất
    operator, price = find_cheapest_operator(phone_number, operators)

    if operator:
        print(f"Nhà viễn thông có giá cước rẻ nhất cho số này là: {operator}, với giá ${price}/phút")
    else:
        print("Không có nhà viễn thông nào có sẵn cho số này.")
