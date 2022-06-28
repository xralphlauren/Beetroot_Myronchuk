import kelvin as k
import unittest


class TestKelvin(unittest.TestCase):

    def test_temp(self):
        self.assertEqual(k.KelvinToFahrenheit(273), 32.0)
        self.assertEqual(int(k.KelvinToFahrenheit(505.78)), 451)
        self.assertEqual(k.KelvinToFahrenheit(1), -457.6)
        self.assertEqual(k.KelvinToFahrenheit(31), -403.6)
        self.assertEqual(k.KelvinToFahrenheit(61), -349.6)
        self.assertEqual(k.KelvinToFahrenheit(91), -295.6)
        self.assertEqual(k.KelvinToFahrenheit(121), -241.60000000000002)
        self.assertEqual(k.KelvinToFahrenheit(151), -187.6)
        self.assertEqual(k.KelvinToFahrenheit(181), -133.6)
        self.assertEqual(k.KelvinToFahrenheit(211), -79.60000000000001)
        self.assertEqual(k.KelvinToFahrenheit(241), -25.6)
        self.assertEqual(k.KelvinToFahrenheit(271), 28.4)
        self.assertEqual(k.KelvinToFahrenheit(301), 82.4)
        self.assertEqual(k.KelvinToFahrenheit(331), 136.4)
        self.assertEqual(k.KelvinToFahrenheit(361), 190.4)
        self.assertEqual(k.KelvinToFahrenheit(391), 244.4)
        self.assertEqual(k.KelvinToFahrenheit(421), 298.40000000000003)
        self.assertEqual(k.KelvinToFahrenheit(451), 352.40000000000003)
        self.assertEqual(k.KelvinToFahrenheit(481), 406.40000000000003)
        self.assertEqual(k.KelvinToFahrenheit(511), 460.40000000000003)
        self.assertEqual(k.KelvinToFahrenheit(541), 514.4000000000001)
        self.assertEqual(k.KelvinToFahrenheit(571), 568.4)
        self.assertEqual(k.KelvinToFahrenheit(601), 622.4)
        self.assertEqual(k.KelvinToFahrenheit(631), 676.4)
        self.assertEqual(k.KelvinToFahrenheit(661), 730.4)
        self.assertEqual(k.KelvinToFahrenheit(691), 784.4)
        self.assertEqual(k.KelvinToFahrenheit(721), 838.4)
        self.assertEqual(k.KelvinToFahrenheit(751), 892.4)
        self.assertEqual(k.KelvinToFahrenheit(781), 946.4)
        self.assertEqual(k.KelvinToFahrenheit(811), 1000.4)
        self.assertEqual(k.KelvinToFahrenheit(841), 1054.4)
        self.assertEqual(k.KelvinToFahrenheit(871), 1108.4)
        self.assertEqual(k.KelvinToFahrenheit(901), 1162.4)
        self.assertEqual(k.KelvinToFahrenheit(931), 1216.4)
        self.assertEqual(k.KelvinToFahrenheit(961), 1270.4)
        self.assertEqual(k.KelvinToFahrenheit(991), 1324.4)


    def test_below_zero(self):
        with self.assertRaises(ValueError):
            k.KelvinToFahrenheit(-5)


    def test_string_in_error(self):
        with self.assertRaises(TypeError):
            k.KelvinToFahrenheit('-5')

if __name__ == '__main__':
    unittest.main()