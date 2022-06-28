import Converter_temp as ct
import unittest


class Converter_test(unittest.TestCase):

    def test_result_check(self):
        self.assertEqual(ct.converter('37C'), (99, 'F', '99F'))
        self.assertEqual(ct.converter('21C'), (70, 'F', '70F'))
        self.assertEqual(ct.converter('50C'), (122, 'F', '122F'))
        self.assertEqual(ct.converter('99F'), (37, 'C', '37C'))
        self.assertEqual(ct.converter('70F'), (21, 'C', '21C'))
        self.assertEqual(ct.converter('122F'), (50, 'C', '50C'))

    def test_type_check(self):
        with self.assertRaises(TypeError):
            ct.converter(15)


if __name__ == '__main__':
    unittest.main()

