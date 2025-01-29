import unittest
import complex as c


class Testcomplex(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(c.sumcplx((1, 2), (3, 4)), (4, 6))
        self.assertEqual(c.sumcplx((5, 8), (10, 6)), (15, 14))

    def test_producto(self):
        self.assertEqual(c.mulcplx((4, 7), (2, 9)), (-55, 50))
        self.assertEqual(c.mulcplx((1, 4), (7, 6)), (-17, 34))

    def test_resta(self):
        self.assertEqual(c.rescplx((9, 1), (5, 3)), (4, -2))
        self.assertEqual(c.rescplx((6, 4), (7, 8)), (-1, -4))

    def test_division(self):
        self.assertEqual(c.divcplx((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(c.divcplx((-1, -2), (3, 4)), (-0.44, -0.08))

    def test_modulo(self):
        self.assertEqual(c.modulo((2,2)), 2.83)
        self.assertEqual(c.modulo((3,8)), 8.54)

    def test_conjugado(self):
        self.assertEqual(c.conjugado((1,2)), (1, -2))
        self.assertEqual(c.conjugado((4,9)), (4, -9))

    def test_polcar(self):
        self.assertEqual(c.pol_car((2,2)), (-0.83, 1.82))
        self.assertEqual(c.pol_car((8,4)), (-5.23, -6.05))

    def test_carpol(self):
        self.assertEqual(c.car_pol((1,1)), (1.41, 0.79))
        self.assertEqual(c.car_pol((6,1)), (6.08, 0.17))

    def fase(self):
        self.assertEqual(c.fase((8,5)), 0.55)
        self.assertEqual(c.fase((7,2)), 0.28)


if __name__ == '__main__':
    unittest.main()

