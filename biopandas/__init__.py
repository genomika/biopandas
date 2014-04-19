"""
biopandas
=========

Biopandas provides tools for the analysis and comprehension of high-throughput genomic data.

It is a project to add support for genomic data to pandas objects.
It is based primarily on the Python programming language.

See further information at https://github.com/genomika/biopandas

"""

__version__ = '0.0.1'


try:
    import pandas as pd
except ImportError:
    raise ImportError('Make sure that you have pandas installed. biopandas requires pandas to install it.',
                           'Do pip install pandas before install biopandas')

import numpy as np

try:
    from numpy.testing import nosetester

    class _NoseTester(nosetester.NoseTester):
        '''
        Subclass numpy's NoseTester to add doctest by default
        '''

        def test(self, label='fast', verbose=1, extra_argv=['--exe'],
            doctests=True, coverage=False):
            return super(_NoseTester, self).test(label=label, verbose=verbose,
                        extra_argv=extra_argv, doctests=doctests, coverage=coverage)
    try:
        test = _NoseTester(raise_warnings='release').test
    except TypeError:
        test = _NoseTester().test

    del nosetester

except:
    pass


