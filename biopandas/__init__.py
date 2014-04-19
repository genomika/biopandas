
try:
    import pandas as pd
except ImportError:
    raise ImportError('Make sure that you have pandas installed. biopandas requires pandas to install it.',
                           'Do pip install pandas before install biopandas')

import numpy as np

