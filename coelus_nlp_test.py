import unittest
from coelus_nlp import pred_or_adj


class PredAdjTest(unittest.TestCase):

    def test_1(self):
        result = pred_or_adj('Я хорош')
        self.assertEqual(result, 'Я хороший')

    def test_2(self):
        result = pred_or_adj('Мне нужно')
        self.assertEqual(result, 'Мне нужно')

    def test_3(self):
        result = pred_or_adj('Он должен')
        self.assertEqual(result, 'Он должен')

    def test_4(self):
        result = pred_or_adj('Я хороша')
        self.assertEqual(result, 'Я хороший')

    def test_5(self):
        result = pred_or_adj('Ему можно')
        self.assertEqual(result, 'Ему можно')

    def test_6(self):
        result = pred_or_adj('Тебе плохо')
        self.assertEqual(result, 'Тебе плохо')

    def test_7(self):
        result = pred_or_adj('Им надо')
        self.assertEqual(result, 'Им надо')


if __name__ == '__main__':
    unittest.main()
