

"Initial File for Redesign_Science."
try:
    from src import version
    __version__ = version.version
except:
    print('__version__ not loaded from file.')
    
try:
    # DATA_PATH = __path__[0] + '/../data'
    DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + '/data'
except:
    print('No DATA_PATH has been set.')
# from __future__ import absolute_import
# import ._omnical, ._Bulm, _boost_math

