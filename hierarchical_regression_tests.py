# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:26:45 2019

@author: BOYLER1
"""

import pandas as pd
import statsmodels.api as sm
import scipy.stats
import numpy as np
import hierarchical_regression

#import os
#curr_dir = os.getcwd()
#os.chdir(r'C:\Users\boyler1\Documents\PhD\Code\cognitive_reserve')
#import hierarchical_regression as h_r
#os.chdir(curr_dir)

# download this data file
# https://courses.edx.org/c4x/MITx/15.071x_2/asset/NBA_train.csv

# read in data
nba = pd.read_csv('./hierarchical_regression/example_dataset/NBA_train.csv')

# prep data
#X = [nba['PTS'], nba[['PTS', 'ORB']], nba[['PTS', 'ORB', 'DRB']]]
nba['interaction'] = nba['PTS'] * nba['ORB']
X = [nba[['PTS']], nba[['PTS', 'ORB']], nba[['PTS', 'ORB', 'interaction']]]
y = nba['W']
names = [['points'], ['points', 'offensive_rebounds'], 
         ['points', 'offensive_rebounds', 'interaction']]

results, models = hierarchical_regression.hierarchical_regression(y, X, names, 'hierarchical_regression')

#runfile('regression_diagnostics.py', wdir='.')
#runfile('hierarchical_regression.py', wdir='.')

model=models[1][1]
result = results.iloc[1]
print(model.summary())
print(results)

#X = X[1]

#saveto = r'C:\Users\boyler1\Documents\PhD\CognitiveReserve\assumptionTest'

#saveFolder = r'C:\Users\boyler1\Documents\PhD\CognitiveReserve\assumptionTest'


#X = predictors
#y = cogFunction
#saveFolder = proxyDir