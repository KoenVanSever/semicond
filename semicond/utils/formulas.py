from numbers import Real

import numpy as np

from .constants import BOLTZ

def to_K(c):
    return c + 273.15

def to_C(k):
    return k - 273.15

def apply_arrhenius(ea : Real, t1 : Real, t2 : Real, x = 1):
    """
    Multiplies :math:`x` with :math:`e^{\\frac{E_{a}}{k_{B} \\cdot (\\frac{1}{T1} - \\frac{1}{T2})}}`.

    :math:`x` can be anything numerical/iterable with numerical values.
    Temperatures are converted to Kelvin within function.

    Parameters
    ----------
    ea : Real
        Activation energy
    t1 : Real
        Temperature 1 in °C
    t2 : Real
        Temperature 2 in °C
    x : Any, default `1`
        Target value
    
    Returns
    -------
    Any
        `x` multiplied with factor.
    """
    return x * np.exp(ea / BOLTZ * ((1 / to_K(t1)) - (1 / to_K(t2)))) # time(T2) = time(T2,init) * e ** (Ea / Hb * ( 1 / T1 - 1 / T2))

def apply_power_law(m : Real, v1: Real, v2: Real, x = 1):
    """
    Multiplies :math:`x` with :math:`x \\cdot (\\frac{v2}{v1})^{m}`.

    :math:`x` can be anything numerical/iterable with numerical values.

    Parameters
    ----------
    m : Real
        Power law exponent
    t1 : Real
        Voltage 1
    t2 : Real
        Voltage 2
    x : Any, default `1`
        Target value
    
    Returns
    -------
    Any
        `x` multiplied with factor.
    """
    return x * (v2/v1) ** m # time(V2) = time(V2,init) * (V2/V1) ** m
