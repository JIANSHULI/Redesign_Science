# from __future__ import absolute_import
# from distutils.core import setup, Extension
import os, glob, numpy
import os.path as op
# from src import version
import json
# from setuptools import Extension, Command
# from setuptools import setup
from distutils.core import setup, Extension
# import version
import numpy as np


########## hera_dp_vs_mp version ###########
__version__ = '1.0.0'

def indir(dir, files): return [dir+f for f in files]
def globdir(dir, files):
    rv = []
    for f in files: rv += glob.glob(dir+f)
    return rv

setup(name = 'Redesign_Science',
    version = __version__,
    # version = version.version,
    description = __doc__,
    long_description = __doc__,
    license = 'GPL',
    author = 'Jianshu Li',
    author_email = '',
    url = 'https://github.com/JIANSHULI/Redesign_Science.git',
    package_dir = {'Redesign_Science':'src'},
    packages = ['Redesign_Science'],
    include_package_data = True,
    ext_modules = [],
    scripts = glob.glob('scripts/*'),
)

from src import version
########## pyuvdata version ##########
data = [version.git_origin, version.git_hash, version.git_description, version.git_branch]
with open(op.join('src', 'GIT_INFO'), 'w') as outfile:
    try:
        json.dump(data, outfile)
    except:
        np.savetxt(outfile, data)
with open(op.join('src', 'VERSION'), 'w') as outfile:
    try:
        json.dump(__version__, outfile)
    except:
        np.savetxt(outfile, __version__)
with open('VERSION', 'w') as outfile:
    try:
        json.dump(__version__, outfile)
    except:
        np.savetxt(outfile, __version__)