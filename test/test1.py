#!/usr/bin/env python
import angles
import numpy as np
import calculation
import uncertainties
import unittest

class SkyPositionTest(unittest.TestCase):
    """docstring """
    def __init__(self, arg):
        self.arg = arg
    
    def test_wrap_works_simple(self):
        """docstring for test_wrap_works_simple"""
        DIP_RA = 17.3
        DIP_RA_ERR = 1.0
        DIP_DEC = -61.0
        DIP_DEC_ERR = 10.0        
        self.assertEqual(calculation.sky_position(DIP_RA, DIP_DEC), calculation.wrapped_sky_position(DIP_RA, DIP_DEC))

# class MonteCarloTest(unittest.TestCase):
#     """docstring for MonteCarloTest"""
#     def __init__(self, arg):
#         super(MonteCarloTest, self).__init__()
#         self.arg = arg
#         
#     def test_mc_theta(self):
#         DIP_RA = 17.3
#         DIP_RA_ERR = 1.0
#         DIP_DEC = -61.0
#         DIP_DEC_ERR = 10.0        
#         first = theta()
#         QSO_RA = "22h20m06.757" # RA
#         QSO_DEC = "-28d03m23.34" # DEC
#         self.assertAlmostEqual(first, second, places=2, msg=None, delta=None)
#         # self.assertEqual()
#         
#     # def test_mc_(self):
#     #     """docstring for test_mc_"""
#     #     assert
# 
# class DipoleErrorTest(unittest.TestCase):
#     """"""
#     def test_theta_transpose(self):
#         """docstring for test_theta"""
#         QSO_POSITION = calculation.QSO_POSITION
#         DIPOLE_POSITION = calculation.DIPOLE_POSITION
#         QSO_DIPOLE_ANGLE = angles.r2d(QSO_POSITION.sep(DIPOLE_POSITION))
#         DIPOLE_QSO_ANGLE = angles.r2d(DIPOLE_POSITION.sep(QSO_POSITION))
#         self.assertEqual(QSO_DIPOLE_ANGLE, DIPOLE_QSO_ANGLE)
#     
#     def test_sky_position_uncertainties(self):
#         """docstring for test_sky_position_uncertainties"""
#         DIP_RA = 17.3
#         DIP_RA_ERR = 1.0
#         DIP_DEC = -61.0
#         DIP_DEC_ERR = 10.0
#         DIPOLE_RA = uncertainties.ufloat((DIP_RA, DIP_RA_ERR))
#         DIPOLE_DEC = uncertainties.ufloat((DIP_DEC, DIP_DEC_ERR))
#         NOMINAL = calculation.sky_position(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value)
#         WRAPPED = calculation.wrapped_sky_position(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value)
#         self.assertAlmostEqual(NOMINAL, WRAPPED)
#         
#     # TODO test that each piece of the equation adds uncertainty
#     # TODO test RA +/- 
#     # TODO test DEC +/- 
#     # TODO test AMPLITUDE +/- 
#     # TODO test MONOPOLE +/- 
#     # TODO test QSO RA
#     # TODO test QSO DEC
#     # #----------------------------------------------------------------------
#     # def test_creation(self):
#     #     """docstring for test_creation"""
#     #     my_obj = calculation.MyClass()
#     #     self.assert_(myobj)
#     
#     # def test_all_ones(self):
#     #     """Constructor"""
#     #     game = Game()
#     #     pins = [1 for i in range(11)]
#     #     game.roll(11, pins)
#     #     self.assertEqual(game.score, 11)

    
if __name__ == "__main__":
    unittest.main()
    
# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)