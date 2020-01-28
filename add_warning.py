import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is None:
         warnings.warn('logfile argument deprecated', DeprecationWarning)
         
func('x','y')