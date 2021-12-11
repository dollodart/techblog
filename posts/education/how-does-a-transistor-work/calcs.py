from numpy import exp, log, sqrt

# physics constants
kB = 1.38e-23  # J/(mol.K)
e = 1.60e-19  # C
# silicon properties
ni = 1e10 * 1e6  # m^-3
# data from http://www.ioffe.ru/SVA/NSM/Semicond/Si/electric.html
Na = 1.6e16 * 1e6  # m^-3
Nd = 2 * Na
Dn = 36e-2 # using the inequality from the source
Dp = 12e-2 # using the inequality from the source
vtn = 2.3e5
vtp = 1.65e5

# thermal properties
T = 300.  # K
beta = 1 / (kB * T)

# let applied voltage be in some ratio with the charge specific thermal energy
arg = 15
Va = arg / beta / e  # V
print(f'Va = {Va:.2E} V such that arg to exponential is {arg}')

ln = sqrt(Dn / vtn)
lp = sqrt(Dp / vtp)
DnoverLn = Dn / ln
DpoverLp = Dp / lp

print(f'Ln/tn = {DnoverLn:.3E} Lp/tp = {DpoverLp:.3E}')

cubic_edge_length = 50e-9
diagram_scale = 5
area = (diagram_scale * cubic_edge_length)**2

# quantity of charge carriers per square meter per second
jovere = (ni**2 * (exp(beta * e * Va) - 1) *
    (DnoverLn / Na + DpoverLp / Nd)) # Marder 19.78

Vt = kB * T / e
# it is important to know what region the charge carriers belong
# to since it is minority carrier dominated.

# electron minority carrier density in p-type region:
n_p0 = ni ** 2 / Na  
# hole minority carrier density in n-type region:
p_n0 = ni ** 2 / Nd
print(f'concentration n={1e6*n_p0:.3E} p={1e6*p_n0:.3E} cm^{-3}')

# check
jovere_alt = ((DnoverLn * n_p0 + DpoverLp * p_n0) *
    (exp(Va / Vt) - 1))  # from Van Zeeghbrook

assert (round(jovere / exp(round(log(jovere))), 6) ==
        round(jovere_alt / exp(round(log(jovere_alt))), 6))

# quantity of charge carriers going through the given
# cross-sectional view, assuming in-page depth equal to width
print(f'current density = {jovere * e:.3E} A / m^2')
print(
    f'current through depicted cross-section = '
    f'{jovere * area:.3E} electrons/s = '
    f'{jovere * area * e:.3E} A')
print(
    f'current through single atom cross-section = '
    f'{jovere * area / diagram_scale**2:.3E} electrons/s = '
    f'{jovere * area * e / diagram_scale **2:.3E} A')


# MOS capacitance
# Na = 1e19*1e6 # degenerate doping
phiF = Vt * log(Na / ni)
eps_sr = 11.9
eps_0 = 8.85418e-12
eps_s = eps_0 * eps_sr
phi_s = 2 * phiF
x = sqrt(2 * eps_s * phi_s / (e * Na))
print(f'p-oxide depletion thickness {x*1e9:.3E} nm')

eps_oxr = 3.9
t_ox = 25e-9
eps_ox = eps_oxr * eps_0
VT = .88  # example 6.2 Van Zeghbrook
VGS = 1.88
Cox = eps_ox / t_ox
qoverarea = Cox * (VGS - VT)
print(f'surface charge for given area '
      f'{qoverarea * area / e:.3E} electrons')
