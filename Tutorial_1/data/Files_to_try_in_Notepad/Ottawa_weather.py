# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 13:42:38 2023

@author: Windows
"""
import pandas as pd

dat = pd.read_pickle(r'C:\Users\Windows\Documents\Ottawa_data.pkl')

datT = dat[dat.Weather=='Snow']

datTgb = datT.groupby([datT.index.year]).count()
datTgb.index.rename('Year',inplace=True)
datTgb.reset_index(inplace=True)
datTgb.set_index('Year',inplace=True,drop=True)


datTgb.Weather.plot()
