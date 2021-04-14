import numpy as np
from math import sqrt


def cubic_spline(index, x0, x, y):
    x = np.asfarray(x)
    y = np.asfarray(y)

    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    A = np.empty(size)
    A_1 = np.empty(size-1)
    s = np.empty(size)

    A[0] = sqrt(2*xdiff[0])
    A_1[0] = 0.0
    B0 = 0.0
    s[0] = B0 / A[0]

    for i in range(1, size-1):
        A_1[i] = xdiff[i-1] / A[i-1]
        A[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - A_1[i-1] * A_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        s[i] = (Bi - A_1[i-1]*s[i-1])/A[i]

    i = size - 1
    A_1[i-1] = xdiff[-1] / A[i-1]
    A[i] = sqrt(2*xdiff[-1] - A_1[i-1] * A_1[i-1])
    Bi = 0.0
    s[i] = (Bi - A_1[i-1]*s[i-1])/A[i]

    i = size-1
    s[i] = s[i] / A[i]
    for i in range(size-2, -1, -1):
        s[i] = (s[i] - A_1[i-1]*s[i+1])/A[i]

    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    si1, si0 = s[index], s[index-1]
    hi1 = xi1 - xi0

    f0 = si0/(6*hi1)*(xi1-x0)**3 + \
         si1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - si1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - si0*hi1/6)*(xi1-x0)
    return f0
