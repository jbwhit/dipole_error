#!/usr/bin/env python
"""Example of dipole_error usage"""
import uncertainties
import dipole_error

# HE2217-2818
QSO_RA = "22 20 06.757" # RA
QSO_DEC = "-28 03 23.34" # DEC
REDSHIFT = 1.6919 # Just pick a redshift to start
RADIAL_DISTANCE = 9.757 # GLyr

#DIP_RA = 17.3
#DIP_RA_ERR = 1.0
#DIP_DEC = -61.0
#DIP_DEC_ERR = 10.0
#DIP_AMPLITUDE = 0.97e-5
#DIP_AMPLITUDE_ERR = 0.21e-5 # average of asymmetric errors
#DIP_MONOPOLE = -0.178e-5
#DIP_MONOPOLE_ERR  = 0.084e-5

# Values and errors combined for uncertainties package.
#DIPOLE_AMPLITUDE = uncertainties.ufloat((DIP_AMPLITUDE, DIP_AMPLITUDE_ERR))
#MONOPOLE = uncertainties.ufloat((DIP_MONOPOLE, DIP_MONOPOLE_ERR))
#DIPOLE_RA = uncertainties.ufloat((DIP_RA, DIP_RA_ERR))
#DIPOLE_DEC = uncertainties.ufloat((DIP_DEC, DIP_DEC_ERR))

#print "Using default inputs: "
#print dipole_error.dipole_monopole()

#print
#print "Different RA values: "
#for ra_value in ["12h20m06.757", 17.2, "17h12m"]:
#    print "RA:", ra_value, "\n  da/a:", dipole_error.dipole_monopole(right_ascension=ra_value, \
#                        declination=QSO_DEC, \
#                        dipole_ra=DIPOLE_RA, \
#                        dipole_dec=DIPOLE_DEC, \
#                        amplitude=DIPOLE_AMPLITUDE, \
#                        monopole=MONOPOLE)
                
#print 
#print "Different DEC values: "
#for dec_value in ["-28d03m23.34", "-61d03m", 15.0]:
#    print "DEC:", dec_value, "\n  da/a:", \
#          dipole_error.dipole_monopole(right_ascension=QSO_RA, \
#                        declination=dec_value, \
#                        dipole_ra=DIPOLE_RA, \
#                        dipole_dec=DIPOLE_DEC, \
#                        amplitude=DIPOLE_AMPLITUDE, \
#                        monopole=MONOPOLE)

#print
#print "Different Amplitude/error values: "
#for amplitude_error in [0.1e-5, 2.0e-5]:
#    print "Amplitude error:", amplitude_error, "\n  da/a:", \
#    dipole_error.dipole_monopole(right_ascension=QSO_RA, \
#                  declination=QSO_DEC, \
#                  dipole_ra=DIPOLE_RA, \
#                  dipole_dec=DIPOLE_DEC, \
#                  amplitude=uncertainties.ufloat((DIP_AMPLITUDE, amplitude_error)), \
#                  monopole=MONOPOLE)
    
#print 
#print "If you want to do it by hand: "
#print dipole_error.dipole_monopole(\
#        right_ascension="22h20m06.757", \
#        declination="-28d03m23.34", \
#        dipole_ra=uncertainties.ufloat((17.3, 1.0)), \
#        dipole_dec=uncertainties.ufloat((-61.0, 10.0)), \
#        amplitude=uncertainties.ufloat((0.97e-5, 0.21e-5)), \
#        monopole=uncertainties.ufloat((-0.178e-5, 0.084e-5)),\
#        )

#print 
#print "If you don't want error, just pass a float (note monopole term):"
#print dipole_error.dipole_monopole(\
#        right_ascension="22h20m06.757", \
#        declination="-28d03m23.34", \
#        dipole_ra=uncertainties.ufloat((17.3, 1.0)), \
#        dipole_dec=uncertainties.ufloat((-61.0, 10.0)), \
#        amplitude=uncertainties.ufloat((0.97e-5, 0.21e-5)), \
#        monopole=0.,\
#        )

#print 
#print "Same functionality with the two other models: z_dipole_monopole and r_dipole_monopole:"

# =====================
# = dipole_only =
# =====================
DIP_RA = 17.4
DIP_RA_ERR = 0.9
DIP_DEC = -58.0
DIP_DEC_ERR = 9.0
DIP_AMPLITUDE = 1.02e-5
DIP_AMPLITUDE_ERR = 0.21e-5 # average of asymmetric errors

# Uncertainties
DIPOLE_AMPLITUDE = uncertainties.ufloat(DIP_AMPLITUDE, DIP_AMPLITUDE_ERR)
MONOPOLE = 0.
DIPOLE_RA = uncertainties.ufloat(DIP_RA, DIP_RA_ERR)
DIPOLE_DEC = uncertainties.ufloat(DIP_DEC, DIP_DEC_ERR)

print "dipole_only"
print dipole_error.dipole_monopole(right_ascension=QSO_RA, \
                      declination=QSO_DEC, \
                      dipole_ra=DIPOLE_RA, \
                      dipole_dec=DIPOLE_DEC, \
                      amplitude=DIPOLE_AMPLITUDE, \
                      monopole=MONOPOLE)


# =====================
# = dipole_monopole =
# =====================
DIP_RA = 17.3
DIP_RA_ERR = 1.0
DIP_DEC = -61.0
DIP_DEC_ERR = 10.0
DIP_AMPLITUDE = 0.97e-5
DIP_AMPLITUDE_ERR = 0.21e-5 # average of asymmetric errors
DIP_MONOPOLE = -0.178e-5
DIP_MONOPOLE_ERR  = 0.084e-5

# Uncertainties
DIPOLE_AMPLITUDE = uncertainties.ufloat(DIP_AMPLITUDE, DIP_AMPLITUDE_ERR)
MONOPOLE = uncertainties.ufloat(DIP_MONOPOLE, DIP_MONOPOLE_ERR)
DIPOLE_RA = uncertainties.ufloat(DIP_RA, DIP_RA_ERR)
DIPOLE_DEC = uncertainties.ufloat(DIP_DEC, DIP_DEC_ERR)

print
print "dipole_monopole"
print dipole_error.dipole_monopole(right_ascension=QSO_RA, \
                      declination=QSO_DEC, \
                      dipole_ra=DIPOLE_RA, \
                      dipole_dec=DIPOLE_DEC, \
                      amplitude=DIPOLE_AMPLITUDE, \
                      monopole=MONOPOLE)


# =====================
# = z_dipole_monopole =
# =====================
Z_DIP_RA = 17.5
Z_DIP_RA_ERR = 1.0
Z_DIP_DEC = -62.0
Z_DIP_DEC_ERR = 10.0
Z_DIP_PREFACTOR = 0.81e-5
Z_DIP_PREFACTOR_ERR = 0.27e-5 # average of .26 and .28
Z_DIP_MONOPOLE = -0.184e-5
Z_DIP_MONOPOLE_ERR = 0.085e-5
Z_DIP_BETA = 0.46
Z_DIP_BETA_ERR = 0.49

Z_DIPOLE_RA = uncertainties.ufloat(Z_DIP_RA, Z_DIP_RA_ERR)
Z_DIPOLE_DEC = uncertainties.ufloat(Z_DIP_DEC, Z_DIP_DEC_ERR)
Z_DIPOLE_PREFACTOR = uncertainties.ufloat(Z_DIP_PREFACTOR, Z_DIP_PREFACTOR_ERR)
Z_DIPOLE_MONOPOLE = uncertainties.ufloat(Z_DIP_MONOPOLE, Z_DIP_MONOPOLE_ERR)
Z_DIPOLE_BETA = uncertainties.ufloat(Z_DIP_BETA, Z_DIP_BETA_ERR)

print
print "z_dipole_monopole: "
print dipole_error.z_dipole_monopole(right_ascension=QSO_RA, \
                      declination=QSO_DEC, \
                      dipole_ra=Z_DIPOLE_RA, \
                      dipole_dec=Z_DIPOLE_DEC, \
                      prefactor=Z_DIP_PREFACTOR, \
                      z_redshift=REDSHIFT, \
                      beta=Z_DIP_BETA, \
                      monopole=Z_DIP_MONOPOLE)

# =====================
# = r_dipole_monopole =
# =====================
R_DIP_RA = 17.5
R_DIP_RA_ERR = 1.0
R_DIP_DEC = -62.0
R_DIP_DEC_ERR = 10.0
R_DIP_AMPLITUDE = 1.1e-6 # in GLyr 
R_DIP_AMPLITUDE_ERR = 0.2e-6 # average of asymmetric errors
R_DIP_MONOPOLE = -0.187e-5
R_DIP_MONOPOLE_ERR  = 0.084e-5

# Uncertainties
R_DIPOLE_AMPLITUDE = uncertainties.ufloat(R_DIP_AMPLITUDE, R_DIP_AMPLITUDE_ERR)
R_DIPOLE_MONOPOLE = uncertainties.ufloat(R_DIP_MONOPOLE, R_DIP_MONOPOLE_ERR)
R_DIPOLE_RA = uncertainties.ufloat(R_DIP_RA, R_DIP_RA_ERR)
R_DIPOLE_DEC = uncertainties.ufloat(R_DIP_DEC, R_DIP_DEC_ERR)

print 
print "r_dipole_monopole"
print dipole_error.r_dipole_monopole(right_ascension=QSO_RA, \
                      declination=QSO_DEC, \
                      dipole_ra=R_DIPOLE_RA, \
                      dipole_dec=R_DIPOLE_DEC, \
                      amplitude=R_DIPOLE_AMPLITUDE, \
                      radial_distance=RADIAL_DISTANCE, \
                      monopole=R_DIPOLE_MONOPOLE)
