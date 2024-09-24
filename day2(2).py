def is_valid_input(num, limit):
    """验证数据是否符合限制"""
    return -limit <= num <= limit

def add(a, b, limit=99):
    """加法"""
    if not is_valid_input(a, limit) or not is_valid_input(b, limit):
        return f"请输入范围为【-{limit}, {limit}】的整数或浮点数"
    return a + b

def subtract(a, b, limit=99):
    """减法"""
    if not is_valid_input(a, limit) or not is_valid_input(b, limit):
        return f"请输入范围为【-{limit}, {limit}】的整数或浮点数"
    return a - b

def multiply(a, b, limit=99):
    """乘法"""
    if not is_valid_input(a, limit) or not is_valid_input(b, limit):
        return f"请输入范围为【-{limit}, {limit}】的整数或浮点数"
    return a * b

def divide(a, b, limit=99):
    """除法"""
    if not is_valid_input(a, limit) or not is_valid_input(b, limit):
        return f"请输入范围为【-{limit}, {limit}】的整数或浮点数"
    # 判断除数是否为0
    if b == 0:
        return "除数不能为0"
    return a / b


class TestCalculator:
    def test_add(self):
        limit = 99
        res1 = add(1, 2, limit)
        res2 = add(100, 9, limit)
        assert res1 == 3
        assert res2 == f"请输入范围为【-{limit}, {limit}】的整数或浮点数"

    def test_subtract(self):
        limit = 100
        res1 = subtract(-99, 99, limit)
        res2 = subtract(102, 2, limit)
        assert res1 == -198
        assert res2 == f"请输入范围为【-{limit}, {limit}】的整数或浮点数"

    def test_multiply(self):
        limit = 80
        res1 = multiply(20, 40, limit)
        res2 = multiply(90, 2, limit)
        assert res1 == 800
        assert res2 == f"请输入范围为【-{limit}, {limit}】的整数或浮点数"

    def test_divide(self):
        limit = 90
        res1 = divide(20, 5, limit)
        res2 = divide(92, 2, limit)
        res3 = divide(90, 0, limit)
        assert res1 == 4.0
        assert res2 == f"请输入范围为【-{limit}, {limit}】的整数或浮点数"
        assert res3 == "除数不能为0"


