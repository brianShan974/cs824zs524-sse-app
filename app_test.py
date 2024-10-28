import unittest
from app import process_query


class TestProcessQuery(unittest.TestCase):
    def test_addition_query(self):
        # 测试加法问题
        self.assertEqual(process_query("What is 67 plus 26?"), "93")
        self.assertEqual(process_query("What is 2 plus 95?"), "97")

    def test_largest_number_query(self):
        # 测试比较大小问题
        self.assertEqual(
            process_query("Which of the following numbers is the largest: 96, 77, 16?"),
            "96",
        )
        self.assertEqual(
            process_query("Which of the following numbers is the largest: 5, 27, 49?"),
            "49",
        )

    def test_unknown_query(self):
        # 测试未知问题
        self.assertEqual(process_query("What is the color of the sky?"), "Unknown")

    def test_subtraction_query(self):
        # 测试减法问题（假设支持此功能）
        self.assertEqual(process_query("What is 100 minus 25?"), "75")

    def test_multiplication_query(self):
        # 测试乘法问题（假设支持此功能）
        self.assertEqual(process_query("What is 7 times 8?"), "56")


if __name__ == "__main__":
    unittest.main()
