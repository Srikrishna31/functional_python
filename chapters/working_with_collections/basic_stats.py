import math
from typing import Sequence
"""
This module contains definitions for basic statistical functions that
can be designed in a functional way
"""


def s0 (samples: Sequence) -> float:
    return sum ( 1 for _ in samples)   # or len(data)


def s1 (samples: Sequence) -> float:
    return sum (x for x in samples)  # or sum(data)


def s2 (samples: Sequence) -> float:
    return sum (x**2 for x in samples)


def mean(samples: Sequence) -> float:
    return s1(samples) / s0(samples)


def std_dev(samples: Sequence) -> float:
    N = s0(samples)
    return math.sqrt(s2(samples) / N - (s1(samples) / N)**2)


def std_value(x: float, m_x: float, s_x: float) -> float:
    """
    This function computes standardized values of a sequence value
    given its mean and standard deviation.
    """
    return (x - m_x) / s_x


def corr(samples1: Sequence, samples2: Sequence) -> float:
    """
    This correlation function gathers basic stastical summaries of the
    two sets of sampes: the mean and standard deviation. Given these
    summaries, we define two generator functions that will create
    normalized values for each set of samples. We can then use the zip()
    function to pair up items from the two sequences of normalized values
    and compute the product of those two normalized values. The average
    of the product of the normalized scores is the correlation.
    """
    m1, s1 = mean(samples1), std_dev(samples1)
    m2, s2 = mean(samples2), std_dev(samples2)
    z1 = (std_value(x, m1, s1) for x in samples1)
    z2 = (std_value(x, m2, s2) for x in samples2)

    return (sum(zx1*zx2 for zx1, zx2 in zip(z1, z2)) / s0(samples1))