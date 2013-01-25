# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# Calculates the expected $d\alpha/\alpha$ from the King, et al. (2012) and error estimate. Section 5.3.

# <codecell>

import angles
import numpy as np

# <codecell>

dipole = angles.AngularPosition(alpha=17.3, delta=-61)

# <codecell>

# Explicit position at surrounding box of errors around dipole position
# RA +/- 1.0 h
# DEC +/- 10 degrees
dipole_p_ra_p_dec = angles.AngularPosition(alpha=18.3, delta=-51)
dipole_p_ra_m_dec = angles.AngularPosition(alpha=18.3, delta=-71)
dipole_m_ra_p_dec = angles.AngularPosition(alpha=16.3, delta=-51)
dipole_m_ra_m_dec = angles.AngularPosition(alpha=16.3, delta=-71)

# <codecell>

# RA and DEC of position under consideration here
# J222
qso = angles.AngularPosition(alpha=22.20, delta=-28.03)
measured_da_a = -1.0904e-6
da_a_stat_error = 2.35e-6
da_a_sys_error = 1.6549e-6

# qso = angles.AngularPosition(alpha=17.30, delta=-60.03) # Test qso position (near dipole)

# <codecell>

# King (2012) eq. 15: da/a = A \cos(\Theta) + m 
def predicted_alpha(A, theta, m):
    """Returns the predicted value of da/a as given by eq. 15 in King et al. 2012
        theta is in radians."""
    return A * np.cos(theta) + m

# <codecell>

# Rahmani 2012  eq. 3
# A = 0.97e-5
# sigma_A = 0.21e-5
# sigma_cos = 
# da_a = 
def sigma(theta):
    """Return the error for a given theta"""
    return np.sqrt((da_a / A)**2 * sigma_A**2 + (da_a / np.cos(theta))**2 * sigma_cos**2)

# <codecell>

# Difference in radians between dipole and qso positions
positions = []
positions.append(np.radians(angles.r2d(qso.sep(dipole)))) # positions[0] is predicted value
positions.append(np.radians(angles.r2d(qso.sep(dipole_p_ra_p_dec))))
positions.append(np.radians(angles.r2d(qso.sep(dipole_p_ra_m_dec))))
positions.append(np.radians(angles.r2d(qso.sep(dipole_m_ra_p_dec))))
positions.append(np.radians(angles.r2d(qso.sep(dipole_m_ra_m_dec))))

# <codecell>

# A and errors
A = 0.97e-5
A_prefactors = []
A_prefactors.append(A) # A_prefactos[0] is predicted value
A_prefactors.append(A + 0.22e-5)
A_prefactors.append(A - 0.20e-5)

# <codecell>

# m and errors
m = -0.178e-5
m_values = []
m_values.append(m) # m_values[0] is predicted value
m_values.append(m - 0.084e-5)
m_values.append(m + 0.084e-5)

# <codecell>

alpha_values = []
for A in A_prefactors:
    for m in m_values:
        for position in positions:
            alpha_values.append(predicted_alpha(A, position, m))
predicted_alpha_value = predicted_alpha(A_prefactors[0], positions[0], m_values[0])
print predicted_alpha_value, np.max(alpha_values), np.min(alpha_values)

# <codecell>

errors = []
errors.append(np.max(alpha_values) - predicted_alpha_value)
errors.append(predicted_alpha_value - np.min(alpha_values))
predicted_error = np.average(errors)

# <codecell>

print predicted_alpha_value, predicted_error

# <codecell>

print "Separation angle between dipole and qso: ", round(np.degrees(positions[0]), 3), \
    "degrees or", round(positions[0], 5), "radians."
print "Predicted da/a: ", round(predicted_alpha_value, 10)
print "Error: ", round(predicted_error, 10)
print "Measured da/a: ", round(measured_da_a, 10)
print "Statistical error: ", round(da_a_stat_error, 10)
print "Systematic error: ", round(da_a_sys_error, 10)
# Add statistical errors in quadrature -- total statistical 
total_error = np.sqrt(predicted_error ** 2 + da_a_stat_error ** 2)
print "Total statistical error (in quad): ", round(total_error, 10)

# Minimize difference between predicted and measured results (within systematic error)
best_difference = np.abs(predicted_alpha_value - measured_da_a) - da_a_sys_error
worst_difference = np.abs(predicted_alpha_value - measured_da_a) + da_a_sys_error
if best_difference < 0:
    # If true
    print "Within systematic error"
else: 
    print "Best sigmas away: ", round(best_difference / total_error, 2)
    print "Worst sigmas away: ", round(worst_difference / total_error, 2)

qso_total_error = np.sqrt(da_a_stat_error ** 2 + da_a_sys_error ** 2)
print qso_total_error
print np.sqrt(qso_total_error ** 2 + predicted_error ** 2)

# <codecell>

# testing 
# plot(linspace(0, (2*np.pi), 360), predicted_alpha(A, linspace(0, (2*np.pi), 360), m))

# Test function working properly
# print A_prefactors[0] + m_values[0],  predicted_alpha(A_prefactors[0], 0, m_values[0])

# Test RA/DEC behaving like expected.
# test1 = angles.AngularPosition(alpha=15.3, delta=-60)
# test2 = angles.AngularPosition(alpha=15.3, delta=-40)
# print angles.r2d(test1.sep(test2)), 20.
# test3 = angles.AngularPosition(alpha=15.3, delta=0)
# test4 = angles.AngularPosition(alpha=14.3, delta=0)
# print angles.r2d(test3.sep(test4)), 360/24.

# Test of what Paolo did to get 5.9 as prediction.
# Didn't work: 
# print predicted_alpha(A_prefactors[0], angles.r2d(qso.sep(dipole)), m_values[0])

# Kanekar 

# <markdowncell>

# Expected da/a at pole
# ======================
# 
# Separation angle between dipole and qso:  0.97 degrees or 0.01693 radians.
# 
# Predicted da/a:  7.9186e-06
# 
# Error:  3.0308e-06
# 
# Measured da/a:  -1.0904e-06
# 
# Statistical error:  2.35e-06
# 
# Systematic error:  1.6549e-06
# 
# Total statistical error (in quad):  3.8352e-06
# 
# Sigmas away:  1.92

# <codecell>

np.sqrt(1.1 ** 2 + 1.4 ** 2)

# <markdowncell>

# Monte Carlo estimation of error
# ==================================

# <codecell>

ra_0 = 17.3
ra_err = 1.0

dec_0 = -61.0
dec_err = 10.0

A_0 = 0.97e-5
A_err = 0.21e-5 # average of upper and lower errors

m_0 = -0.178e-5
m_err = 0.084e-5

def monte_carlo(value, error):
    """Return a random value around value +/- error"""
    return np.random.normal(value, error)

def monte_carlo_angle():
    return np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=monte_carlo(ra_0, ra_err), delta=monte_carlo(dec_0, dec_err)))))

#alpha_mc = np.random.normal(ra_0, ra_err)
#delta_mc = np.random.normal(dec_0, dec_err)
#print alpha_mc, delta_mc
# np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=alpha_mc, delta=delta_mc))))

# <codecell>

predicted_alpha(monte_carlo(A_0, A_err), monte_carlo_angle(), monte_carlo(m_0, m_err))

# <codecell>

alpha_mc = [predicted_alpha(monte_carlo(A_0, A_err), monte_carlo_angle(), monte_carlo(m_0, m_err)) for x in range(100000)]

# <codecell>

print np.average(alpha_mc), np.std(alpha_mc)
print predicted_alpha(A_0, positions[0], m_0)
print np.degrees(positions[0])
print np.degrees(np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=ra_0, delta=dec_0)))))
print predicted_alpha(A_0, np.degrees(np.radians(angles.r2d(qso.sep(angles.AngularPosition(alpha=A_0, delta=dec_0))))), m_0)

# <codecell>

print "Separation angle between dipole and qso: ", round(np.degrees(positions[0]), 3), \
    "degrees or", round(positions[0], 5), "radians."
predicted_alpha_value = predicted_alpha(A_prefactors[0], positions[0], m_values[0])
monte_carlo_alpha = np.average(alpha_mc)
monte_carlo_error = np.std(alpha_mc)
print "Predicted da/a: ", round(predicted_alpha_value, 10)
print "Monte Carlo da/a: ", round(monte_carlo_alpha, 10)
print "Monte Carlo error: ", round(monte_carlo_error, 10)
print "Measured da/a: ", round(measured_da_a, 10)
print "Statistical error: ", round(da_a_stat_error, 10)
print "Systematic error: ", round(da_a_sys_error, 10)
# Add statistical errors in quadrature -- total statistical 
total_error = np.sqrt(monte_carlo_error ** 2 + da_a_stat_error ** 2)
print "Total statistical error (in quad): ", round(total_error, 10)

# Minimize difference between predicted and measured results (within systematic error)
best_difference = np.abs(predicted_alpha_value - measured_da_a) - da_a_sys_error
worst_difference = np.abs(predicted_alpha_value - measured_da_a) + da_a_sys_error
if best_difference < 0:
    # If true
    print "Within systematic error"
else: 
    print "Best sigmas away: ", round(best_difference / total_error, 2)
    print "Worst sigmas away: ", round(worst_difference / total_error, 2)

qso_total_error = np.sqrt(da_a_stat_error ** 2 + da_a_sys_error ** 2)
print qso_total_error
print np.sqrt(qso_total_error ** 2 + monte_carlo_error ** 2)

# <codecell>


# <codecell>

cospositions = [np.cos(x) for x in positions]

# <codecell>

cosposition_err = np.max(cospositions) - np.min(cospositions)

# <codecell>

np.sqrt(np.cos(positions[0])**2 * A_err**2 + A**2 * cosposition_err**2 + 1**2 * m_err**2)

# <codecell>

np.sqrt(np.cos(positions[0])**2 * A_err**2 + A_0**2 * (cosposition_err/2)**2 + 1**2 * m_err**2)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


