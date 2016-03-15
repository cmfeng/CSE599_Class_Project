'''Units test for plot_x_vs_y.py'''

import unittest

import numpy as np
import pandas as pd

from plot_x_vs_y import plot_x_vs_y

class TestDownload(unittest.TestCase):
    #Test to make sure that the plot saves successfully
    def testPlotSaves(self):
        #Make fake data frame to test code
        data = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])
        result = plot_x_vs_y(data, 'A', 'B', 'a_vs_b')
        expected_result = 'Figure a_vs_b successfully saved.'
        self.assertEqual(result, expected_result)

    #Test to make sure that the function throws an error if the column names
    #   are incorrect
    def testColumnNames(self):
        #Make fake data frame to test code
        data = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])
        result = plot_x_vs_y(data, 'Apple', 'B', 'a_vs_b')
        expected_result = 'Please verify column names are correct.'
        self.assertEqual(result, expected_result)

    #Test to make sure that the function throws an error if the data frame is
    #   empty
    def testEmptyDataFrame(self):
        #Make fake data frame to test code
        data = []
        result = plot_x_vs_y(data, 'A', 'B', 'a_vs_b')
        expected_result = 'Please enter valid data frame.'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
