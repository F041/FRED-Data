# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:02:32 2023

@author: Gabriele
"""

import os
from fredapi import Fred
api_key = os.getenv('FRED_API_KEY')
def get_latest():
    fred = Fred(api_key=api_key)
    data = fred.get_series('RECPROUSM156N')
    latest_value = data.iloc[-1]
    return(latest_value)

get_latest()
