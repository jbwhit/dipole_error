#!/usr/bin/env python
"""Calculates the expected $\Delta \alpha/\alpha$ from the King, et al. (2012) and error estimate. Section 5.3."""
import angles
import numpy as np
import uncertainties

# King et al. (2012) dipole location
DIP_RA = 17.3
DIP_RA_ERR = 1.0
DIP_DEC = -61.0
DIP_DEC_ERR = 10.0

DIPOLE_RA = uncertainties.ufloat((DIP_RA, DIP_RA_ERR))
DIPOLE_DEC = uncertainties.ufloat((DIP_DEC, DIP_DEC_ERR))

QSO_RA = "22h20m06.757" # RA
QSO_DEC = "-28d03m23.34" # DEC
# QSO_decimal_RA = 335.028153 
# QSO_decimal_DEC = -28.056483
QSO_decimal_RA = 335.028153 
QSO_decimal_DEC = -28.056483
DIP_decimal_RA = angles.h2d(DIP_RA)
DIP_decimal_DEC = angles.h2d(DIP_DEC)

# np.degrees(jw_sep(QSO_decimal_RA, QSO_decimal_DEC, DIP_decimal_RA, DIP_decimal_DEC)) # 58.032267492266556

def sky_position(right_ascension, declination):
    """docstring for qso_position"""
    return angles.AngularPosition(alpha=right_ascension, delta=declination)

wrapped_sky_position = uncertainties.wrap(sky_position)

QSO_POSITION = sky_position(QSO_RA, QSO_DEC)
DIPOLE_POSITION = sky_position(DIP_RA, DIP_DEC)
# print "QSO_POSITION: ", QSO_POSITION
# print "DIPOLE_POSITION: ", sky_position(DIP_RA, DIP_DEC)

def monte_carlo(value, error):
    """Return a random value around value +/- error"""
    if error == 0:
        return value
    else:
        return np.random.normal(value, error)

def monte_carlo_angle(right_ascension, right_ascension_error, declination, declination_error, qso=QSO_POSITION):
    """Return the radians between the two points """
    # return np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=monte_carlo(ra_0, ra_err), delta=monte_carlo(dec_0, dec_err)))))
    return np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=monte_carlo(right_ascension, right_ascension_error), delta=monte_carlo(declination, declination_error)))))


def mc_theta(right_ascension, \
            declination, qso=sky_position(QSO_RA, QSO_DEC), *args, **kwargs):
    """docstring for mc_theta"""
    dipole_sky_position = angles.AngularPosition(alpha=right_ascension, delta=declination)
    return np.radians(angles.r2d(qso.sep(dipole_sky_position)))

def theta(right_ascension, declination, qso=sky_position(QSO_RA, QSO_DEC), *args, **kwargs):
    """Returns the radian angle between two RA and DECs.
    
    Arguments:
    :param right_ascension: right ascension of position, e.g., "22h20m06.757"
    :type right_ascension: string
    :param declination: declination of position, e.g., "-28d03m23.34"
    :type declination: string
    :param qso: angles position of point on sky
    :type qso: number
    """
    dipole_sky_position = angles.AngularPosition(alpha=right_ascension, delta=declination)
    return np.radians(angles.r2d(qso.sep(dipole_sky_position)))

uncertainty_theta = uncertainties.wrap(theta)
def theta2(dipole_ra, dipole_dec, qso_ra, qso_dec):
    return np.radians(angles.r2d(sky_position(qso_ra, qso_dec).sep(sky_position(dipole_ra, dipole_dec))))

def theta3(dipole_ra, dipole_dec, qso_ra, qso_dec):
    # dipole_sky_position = angles.AngularPosition(alpha=dipole_ra, delta=dipole_dec)
    dipole_sky_position = sky_position(dipole_ra, dipole_dec)
    # qso_position = angles.AngularPosition(alpha=qso_ra, delta=qso_dec)
    qso_position = sky_position(qso_ra, qso_dec)
    return np.radians(angles.r2d(qso_position.sep(dipole_sky_position)))

uncertainty_theta = uncertainties.wrap(theta)
uncertainty_theta2 = uncertainties.wrap(theta2)
uncertainty_theta3 = uncertainties.wrap(theta3)
    
# print "Test 1:", theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION)
# print "Test 2:", uncertainty_theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION)
# print "Test 3:", uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=QSO_POSITION)
# print "Test 4:", uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=sky_position(QSO_RA, QSO_DEC))
# print "Test 5:", uncertainty_theta2(DIPOLE_RA, DIPOLE_DEC, QSO_RA, QSO_DEC)
# print "Test 5a:", theta2(DIPOLE_RA, DIPOLE_DEC, QSO_RA, QSO_DEC)
# print "Test 5b:", theta3(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, QSO_RA, QSO_DEC)
# print "Test 5c:", uncertainty_theta3(DIPOLE_RA, DIPOLE_DEC, QSO_RA, QSO_DEC)

A_0 = 0.97e-5
A_ERR = 0.21e-5 # average of asymmetric errors
AMPLITUDE = uncertainties.ufloat((A_0, A_ERR))

M_0 = -0.178e-5
M_ERR  = 0.084e-5
MONOPOLE = uncertainties.ufloat((M_0, M_ERR))

def dipole_monopole(amplitude=AMPLITUDE, theta=uncertainty_theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), monopole=MONOPOLE, *args, **kwargs):
    """Returns the predicted value of da/a as given by eq. 15 in King et al. 2012.
    
    Arguments:
    :param amplitude: Amplitude of dipole.
    :type amplitude: number
    :param theta: angle in radians between two positions considered on sky.
    :type theta: number
    :param monopole: monopole term.
    :type monopole: number
    :returns: value of predicted dipole at a theta radians away from dipole.
    :rtype: number
    """
    return amplitude * np.cos(theta) + monopole

def dipole_monopole2(amplitude=AMPLITUDE, theta=uncertainty_theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), monopole=MONOPOLE, *args, **kwargs):
    """Returns the predicted value of da/a as given by eq. 15 in King et al. 2012.

    Arguments:
    :param amplitude: Amplitude of dipole.
    :type amplitude: number
    :param theta: angle in radians between two positions considered on sky.
    :type theta: number
    :param monopole: monopole term.
    :type monopole: number
    :returns: value of predicted dipole at a theta radians away from dipole.
    :rtype: number
    """
    return amplitude * uncertainties.math.cos(theta) + monopole


uncertainty_dipole_monopole = uncertainties.wrap(dipole_monopole)
uncertainty_dipole_monopole2 = uncertainties.wrap(dipole_monopole2)

# print "Test 6:", dipole_monopole(AMPLITUDE.nominal_value, theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), MONOPOLE.nominal_value)
# print "Test 7:", uncertainty_dipole_monopole(AMPLITUDE.nominal_value, \
#                                             theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), MONOPOLE.nominal_value)
# print "Test 8 (Amp):", uncertainty_dipole_monopole(AMPLITUDE, theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), MONOPOLE.nominal_value)
# print "Test 9 (Mono):", uncertainty_dipole_monopole(AMPLITUDE.nominal_value, theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), MONOPOLE)
# print "Test 10 (Amp/Mono):", uncertainty_dipole_monopole(AMPLITUDE, theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION), MONOPOLE)
# print "Test 11 (all):", uncertainty_dipole_monopole(AMPLITUDE, uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=QSO_POSITION), MONOPOLE)
# 
# dipole_monopole_dict = {
#     'amplitude': AMPLITUDE,
#     'theta': uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=QSO_POSITION),
#     'monopole': MONOPOLE,
# }
# 
# # print dipole_monopole_dict
# print uncertainty_dipole_monopole(**dipole_monopole_dict)
# print uncertainty_dipole_monopole(theta=uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=QSO_POSITION))
# print "Test 13", uncertainty_dipole_monopole2(theta=uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=QSO_POSITION))
# print "Test 12:", uncertainty_dipole_monopole(theta=uncertainty_theta(DIPOLE_RA, DIPOLE_DEC, qso=sky_position("22h20m06.757", "-28d03m23.34")))
# print dipole_monopole(theta=uncertainty_theta(DIPOLE_RA.nominal_value, DIPOLE_DEC.nominal_value, qso=QSO_POSITION))
# 
# 
# 
# 
# # wrapped_f = uncertainties.wrap(predicted_alpha)
# # x = uncertainties.ufloat((A_0, A_err))
# # y = uncertainties.ufloat((m_0, m_err))
# # raz = uncertainties.ufloat((ra_0, ra_err))
# # 
# 
# # measured_da_a = -1.0904e-6
# # da_a_stat_error = 2.35e-6
# # da_a_sys_error = 1.6549e-6
# 
# # print "Test3:", dipole2(QSO_RA, QSO_DEC, raz, decz)
# # 
# # 
# # numerical_alpha_error =  wrapped_f(x, wrapped_dipole_angle(raz, decz), y)
# # print numerical_alpha_error
# # 
# # measured_da_a_error = uncertainties.ufloat((measured_da_a, da_a_stat_error))
# # numerical_alpha_error.std_score(measured_da_a_error)
# 
# # print uncertainty_theta(right_ascension=QSO_RA, declination=QSO_DEC, **dipole_monopole_dict)
# # print uncertainty_dipole_monopole(theta=uncertainty_theta(right_ascension=QSO_RA, declination=QSO_DEC, **dipole_monopole_dict), **dipole_monopole_dict)    
# # def dipole_only(amplitude, theta, **kwargs):
# #     """Returns the predicted value of da/a as given by S5.3 in King et al. 2012.
# #     
# #     Arguments:
# #     :param amplitude: Amplitude of dipole.
# #     :type amplitude: number
# #     :param theta: angle in radians between two positions considered on sky.
# #     :type theta: number
# #     """
# #     return amplitude * np.cos(theta)
# # 
# # 
# # def z_dipole_monopole(amplitude, redshift, beta, theta, monopole, **kwargs):
# #     """Returns the predicted da/a given by eq. 18 in King et al. 2012.
# #     
# #     Arguments:
# #     :param amplitude: Amplitude of dipole.
# #     :type amplitude: number
# #     :param redshift: Redshift of position considered.
# #     :type redshift: number
# #     :param beta: power law exponent.
# #     :type beta: number
# #     :param theta: angle in radians between two positions considered on sky.
# #     :type theta: number    
# #     :param monopole: monopole term.
# #     :type monopole: number
# #     """
# #     return amplitude * redshift ** (beta) * np.cos(theta) + monopole
# #     
# # def r_dipole_monopole(amplitude, distance, theta, monopole, **kwargs):
# #     """Returns the predicted da/a given by eq. 19 in King et al. 2012
# #     
# #     Arguments:
# #     :param amplitude: Amplitude of dipole.
# #     :type amplitude: number
# #     :param distance: Distance of position considered in G Lyr.
# #     :type distance: number
# #     :param theta: angle in radians between two positions considered on sky.
# #     :type theta: number    
# #     :param monopole: monopole term.
# #     :type monopole: number
# #     """
# #     return amplitude * distance * np.cos(theta) + monopole
# #     
# #     
# # def r_dipole_only(amplitude, distance, theta, **kwargs):
# #     """Returns the predicted da/a given by eq. 20 in King et al. 2012
# #     
# #     Arguments:
# #     :param amplitude: Amplitude of dipole.
# #     :type amplitude: number
# #     :param distance: Distance of position considered in G Lyr.
# #     :type distance: number
# #     :param theta: angle in radians between two positions considered on sky.
# #     :type theta: number    
# #     :param monopole: monopole term.
# #     :type monopole: number
# #     """
# #     return amplitude * distance * np.cos(theta)
# # 
# # models = {
# #     dipole_monopole
# # }
# # # dipole = angles.AngularPosition(alpha=17.3, delta=-61)
# 
# # RA and DEC of position under consideration here
# # J222
# # qso = angles.AngularPosition(alpha=22.20, delta=-28.03)
# # measured_da_a = -1.0904e-6
# # da_a_stat_error = 2.35e-6
# # da_a_sys_error = 1.6549e-6
# 
# 
# # 
# # x = uncertainties.ufloat((A_0, A_err))
# # y = uncertainties.ufloat((m_0, m_err))
# # raz = uncertainties.ufloat((ra_0, ra_err))
# # decz = uncertainties.ufloat((dec_0, dec_err))
# # 
# 
# # positions.append(np.radians(angles.r2d(qso.sep(dipole_m_ra_m_dec))))
# # print "Separation angle between dipole and qso: ", round(np.degrees(positions[0]), 3), \
# #     "degrees or", round(positions[0], 5), "radians."
# # print "Predicted da/a: ", round(predicted_alpha_value, 10)
# # print "Error: ", round(predicted_error, 10)
# # print "Measured da/a: ", round(measured_da_a, 10)
# # print "Statistical error: ", round(da_a_stat_error, 10)
# # print "Systematic error: ", round(da_a_sys_error, 10)
# # # Add statistical errors in quadrature -- total statistical 
# # total_error = np.sqrt(predicted_error ** 2 + da_a_stat_error ** 2)
# # print "Total statistical error (in quad): ", round(total_error, 10)
# # 
# # # Minimize difference between predicted and measured results (within systematic error)
# # best_difference = np.abs(predicted_alpha_value - measured_da_a) - da_a_sys_error
# # worst_difference = np.abs(predicted_alpha_value - measured_da_a) + da_a_sys_error
# # if best_difference < 0:
# #     # If true
# #     print "Within systematic error"
# # else: 
# #     print "Best sigmas away: ", round(best_difference / total_error, 2)
# #     print "Worst sigmas away: ", round(worst_difference / total_error, 2)
# # 
# # qso_total_error = np.sqrt(da_a_stat_error ** 2 + da_a_sys_error ** 2)
# # print qso_total_error
# # print np.sqrt(qso_total_error ** 2 + predicted_error ** 2)
# # 
# # 
# # # testing 
# # # plot(linspace(0, (2*np.pi), 360), predicted_alpha(A, linspace(0, (2*np.pi), 360), m))
# # 
# # # Test function working properly
# # # print A_prefactors[0] + m_values[0],  predicted_alpha(A_prefactors[0], 0, m_values[0])
# # 
# # # Test RA/DEC behaving like expected.
# # # test1 = angles.AngularPosition(alpha=15.3, delta=-60)
# # # test2 = angles.AngularPosition(alpha=15.3, delta=-40)
# # # print angles.r2d(test1.sep(test2)), 20.
# # # test3 = angles.AngularPosition(alpha=15.3, delta=0)
# # # test4 = angles.AngularPosition(alpha=14.3, delta=0)
# # # print angles.r2d(test3.sep(test4)), 360/24.
# # 
# # # Test of what Paolo did to get 5.9 as prediction.
# # # Didn't work: 
# # # print predicted_alpha(A_prefactors[0], angles.r2d(qso.sep(dipole)), m_values[0])
# # 
# # # Kanekar 
# # 
# # # <markdowncell>
# # 
# # # Expected da/a at pole
# # # ======================
# # # Separation angle between dipole and qso:  0.97 degrees or 0.01693 radians.
# # # Predicted da/a:  7.9186e-06
# # # Error:  3.0308e-06
# # # Measured da/a:  -1.0904e-06
# # # Statistical error:  2.35e-06
# # # Systematic error:  1.6549e-06
# # # Total statistical error (in quad):  3.8352e-06
# # # Sigmas away:  1.92
# # 
# # 
# # # np.sqrt(1.1 ** 2 + 1.4 ** 2)
# # 
# # print np.average(alpha_mc), np.std(alpha_mc)
# # print predicted_alpha(A_0, positions[0], m_0)
# # print np.degrees(positions[0])
# # print np.degrees(np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=ra_0, delta=dec_0)))))
# # print predicted_alpha(A_0, np.degrees(np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=A_0, delta=dec_0))))), m_0)
# # 
# # 
# # print "Separation angle between dipole and qso: ", round(np.degrees(positions[0]), 3), \
# #     "degrees or", round(positions[0], 5), "radians."
# # predicted_alpha_value = predicted_alpha(A_prefactors[0], positions[0], m_values[0])
# # monte_carlo_alpha = np.average(alpha_mc)
# # monte_carlo_error = np.std(alpha_mc)
# # print "Predicted da/a: ", round(predicted_alpha_value, 10)
# # print "Monte Carlo da/a: ", round(monte_carlo_alpha, 10)
# # print "Monte Carlo error: ", round(monte_carlo_error, 10)
# # print "Measured da/a: ", round(measured_da_a, 10)
# # print "Statistical error: ", round(da_a_stat_error, 10)
# # print "Systematic error: ", round(da_a_sys_error, 10)
# # # Add statistical errors in quadrature -- total statistical 
# # total_error = np.sqrt(monte_carlo_error ** 2 + da_a_stat_error ** 2)
# # print "Total statistical error (in quad): ", round(total_error, 10)
# # 
# # # Minimize difference between predicted and measured results (within systematic error)
# # best_difference = np.abs(predicted_alpha_value - measured_da_a) - da_a_sys_error
# # worst_difference = np.abs(predicted_alpha_value - measured_da_a) + da_a_sys_error
# # if best_difference < 0:
# #     # If true
# #     print "Within systematic error"
# # else: 
# #     print "Best sigmas away: ", round(best_difference / total_error, 2)
# #     print "Worst sigmas away: ", round(worst_difference / total_error, 2)
# # 
# # qso_total_error = np.sqrt(da_a_stat_error ** 2 + da_a_sys_error ** 2)
# # print qso_total_error
# # print np.sqrt(qso_total_error ** 2 + monte_carlo_error ** 2)
# # 
# # 
# # cospositions = [np.cos(x) for x in positions]
# # cosposition_err = np.max(cospositions) - np.min(cospositions)
# # np.sqrt(np.cos(positions[0])**2 * A_err**2 + A**2 * cosposition_err**2 + 1**2 * m_err**2)
# # np.sqrt(np.cos(positions[0])**2 * A_err**2 + A_0**2 * (cosposition_err/2)**2 + 1**2 * m_err**2)
