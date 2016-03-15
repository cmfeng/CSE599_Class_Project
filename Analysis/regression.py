"""regression.py"""

from __future__ import print_function

import os
import pandas as pd
import numpy as np
import random
import math

import matplotlib.pyplot as plt
from matplotlib import gridspec

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def random_model(data):
    """
    This function selects a random dependent variable y and 4 random
    covariates of type float64 from a data set for a regression model
    """

    # Find variables in the data set with dtype float64
    vars = list(data.columns[data.dtypes == 'float64'])

    # Select a random dependent variable y
    y = random.sample(vars, 1)[0]

    # Select 4 random independent variables x1, x2, x3, x4
    vars.remove(y)
    randomVars = random.sample(vars, 4)

    # Define the formula as a string
    formulaStr = '%s ~ %s + %s + %s + %s' %(y, randomVars[0], randomVars[1], randomVars[2], randomVars[3])

    return(data, y, randomVars, formulaStr);


def compare_OLS(data):
    """
    This function runs an ordinary least squares regression on data
    generated by the random_model function, using both the statsmodels
    and scikit-learn packages, for comparison purposes.
    """

    # Generate a random model, using the random_model() function
    rmod = random_model(data)
    dat = rmod[0]  # the imported data set from random_model function

    # Run a statsmodels OLS regression on y vs 4 random covariates
    print('statsmodels OLS regression on \n %s' % rmod[3])
    mod1 = smf.ols(formula = str(rmod[3]), data=dat).fit()
    # print('Parameters: ', mod1.params)
    # print('R2: ', mod1.rsquared)
    # print('AIC: ', mod1.aic)
    # print('BIC: ', mod1.bic)
    print('\n', mod1.summary(), '\n')

    # Run a scikit-learn OLS regression on the same model
    print('\n scikit-learn OLS regression on \n %s' % rmod[3], '\n')
    y = dat[rmod[1]]
    x = dat[rmod[2]]
    mod2 = LinearRegression()
    mod2.fit(x, y)
    print(mod2.intercept_)
    print(mod2.coef_)
    print(mod2.score(x, y))


def user_model(data):
    """
    This function allows the user to enter their own linear regression
    model formula, which is then run in the statsmodels package and
    returns model results.
    """

    # List available covariates in the data set
    print('The data set contains the following covariates: \n')
    print(list(data.columns), '\n')

    # Prompt user to input model formula, in R type syntax
    userFormula = choose_data = input('Enter your regression model formula, using syntax as shown: \n \n dependent_variable ~ covariate1 + covariate 2 + ... \n \n')

    # Run the user-defined model as a statsmodels linear regression
    userModel = smf.ols(formula=userFormula, data=data).fit()
    print('\n', userModel.summary(), '\n')

    # Retrieve y variable and time variable for plotting
    yvar = userModel.model.endog_names
    y = data[yvar]
    timeVar = list(data.columns[data.dtypes == 'datetime64[ns]'])
    x = data[timeVar]
    # covars = list(userModel.params.keys())


    # Plot dependent variable data and model fitted values vs time
    prstd, iv_l, iv_u = wls_prediction_std(userModel)
    fig = plt.figure(figsize=(12,6))

    plt.plot(x, userModel.fittedvalues, 'r.', alpha=0.2, label='Fitted Values')
    plt.plot(x, y, 'b.', alpha=0.2, label='%s data' % yvar)
    plt.legend(loc='upper left')
    plt.title('%s actual data and model fitted values' % yvar, fontsize='x-large')


def correl(x, y):
    """
    Compute Pearson correlation coefficient (r-squared)
    """

    # Normalize X and Y
    x -= x.mean(0)
    y -= y.mean(0)
    x /= x.std(0)
    y /= y.std(0)

    # Compute mean product (r-squared)
    return (np.mean(x*y)**2)


def find_correlations(data, minCorr=0.2, maxCorr=0.9):
    """
    This function finds correlated variables within a data set,
    and stores the correlated pairs in a data frame along with
    the Pearson correlation coefficient (r-squared).

    The function takes as arguments the data set, and minimum
    and maximum correlation values of interest (0.2 - 0.9 by default).
    """
    # Identify float64 variables in the data set
    floatVars = list(data.columns[data.dtypes == 'float64'])
    floatData = data[floatVars]
    nParams = len(floatVars)

    # Initialize a dataframe to store correlated pairs
    pairs = pd.DataFrame(columns = ['x','y','corr'])

    # Find correlated variables, and store them in the dataframe
    k=0
    for i in range(0, nParams-1):
        for j in range(i+1, nParams):
            corr = round(correl(floatData.iloc[:,i], floatData.iloc[:,j]),3)
            if minCorr < corr < maxCorr:
                pairs.loc[k] = [floatVars[i], floatVars[j], corr]
            k = k+1

    return pairs.set_index([list(range(len(pairs)))])


def plot_pairs(data, minCorr=0.2, maxCorr=0.9):
    """
    This function looks for correlated variables within a data set,
    and then creates a grid of scatterplots of correlated pairs, with
    the r-squared value in the title of each subplot.
    """
    # Call find_correlations function to get correlated pairs
    pairs = find_correlations(data, minCorr, maxCorr)

    # Set plot grid to necessary number of rows by 4 cols (if data cols >4)
    if len(pairs) > 3:
        cols = 4
        rows = int(math.ceil(len(pairs) / cols))
        gs = gridspec.GridSpec(rows, cols)
        fig = plt.figure(figsize=(12,3*rows))
    elif len(pairs) == 0:
        print('No correlations between %s and %s for this data set' % (minCorr, maxCorr))
        return
    else:
        cols = len(pairs)
        rows = 1
        gs = gridspec.GridSpec(rows, cols)
        fig = plt.figure(figsize=(3*cols, 3*rows))

    # Plot each correlated pair on a subplot
    for i in range(0,len(pairs)):
        ax = fig.add_subplot(gs[i])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel('%s' % str(pairs.loc[i][0]), fontsize=14)
        ax.set_ylabel('%s' % pairs.loc[i][1], fontsize=14)
        ax.set_title('$r^2$ = %s' % str(pairs.loc[i][2]), fontsize=14)
        ax.plot(data[pairs.loc[i][0]], data[pairs.loc[i][1]], 'b.', alpha=0.1)
    fig.tight_layout(pad=3)
