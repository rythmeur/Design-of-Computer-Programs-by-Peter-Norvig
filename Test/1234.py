from __future__ import division  # always use floating point division
import numpy as np  # convention, use alias ``np``

# a one dimensional array
x = np.array([2, 7, 5])
print 'x:', x  # print x

# a sequence starting from 4 to 12 with a step size of 3
y = np.arange(4, 12, 3)
print 'y:', y

# element-wise operations on arrays
print 'x + y:', x + y
print 'x / y:', x / y
print 'x ^ y:', x ** y  # python uses ** for exponentiation

import rpy2.rinterface as rinterface
import rpy2.robjects as robjects


pi = robjects.r['pi']
print pi[0]
