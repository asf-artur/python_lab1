import pandas
import zagruzka
import unittest


def collectData():
    return zagruzka.main()


# def collectDataTest():
#     d1 = {'s1': [100, 120, 140, 170]}
#     d1['s2'] = [120, 110, 145, 165]
#     d1['s3'] = [160, 145, 140, 150]
#     d1['s4'] = [185, 170, 175, 190]
#     dt = pandas.DataFrame(d1, index=['A1','A2','A3'])
#     return dt

def collectDataTest():
    mas = [i for i in range(5)]
    return mas


def ChastInervals(mas: list):
    pass


class TestClass(unittest.TestCase):
    def test1(self):
        expected = [
            [0, 2.5],
            [2.5, 5],
            [5, 5]
        ]
        testMas = collectDataTest()
        actual = ChastInervals(testMas)
        self.assertEqual(expected, actual)
        unittest.TestRunner

unittest.main()