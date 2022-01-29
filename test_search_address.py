import unittest

from search_address import search_address


class MyTestCase(unittest.TestCase):
    def test_郵便番号が住所と合致する(self):
        actual = search_address("0287302")
        expected = [
            "岩手県八幡平市八幡平温泉郷",
            "岩手県八幡平市松尾寄木",
            "岩手県八幡平市松川温泉",
        ]
        self.assertEqual(expected, actual)

    def test_郵便番号が7桁以外(self):
        actual = search_address("00")
        expected = "郵便番号はハイフンなしの7桁で入力してください！(*｀･ω･´)"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
