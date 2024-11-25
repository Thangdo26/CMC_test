# Cheapest Operator Finding 
# Author: Đỗ Đình Thắng

This program determines the cheapest operator for a given phone number based on provided price lists.

## How to Use

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Clone the repository:
   ```python
   python cheapest_operator.py
3. Run tests:
   ```python
   python test_cheapest_operator.py
4. Luồng hoạt động khi chạy:
Input:
phone_number = "4673212345"
operators = [OperatorPriceList("Operator A", {...}), OperatorPriceList("Operator B", {...})]
Các bước:
Duyệt qua Operator A:

Gọi get_price("4673212345"):
Prefix dài nhất là 46732.
Giá cước là 1.1.
So sánh giá 1.1 với cheapest_price (float('inf')):
Cập nhật: cheapest_price = 1.1, cheapest_operator = "Operator A".
Duyệt qua Operator B:

Gọi get_price("4673212345"):
Prefix dài nhất là 467.
Giá cước là 1.0.
So sánh giá 1.0 với cheapest_price (1.1):
Cập nhật: cheapest_price = 1.0, cheapest_operator = "Operator B".
Trả về kết quả:

("Operator B", 1.0).
