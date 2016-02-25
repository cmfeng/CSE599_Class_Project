''' Unit tests for lake_utils.py '''

import unittest
from lake_utils import plot_CH4
from lake_utils import merge_data
import os


class TestProntoUtils(unittest.TestCase):

    #Did the csv actually export and save? 
    def testDatasave(self):
        self.assertTrue(os.path.exists('merged_data.csv'), "Failed to save the merged data.")
        

    #Did the plot actually export and save? 
    def testPlotsave(self):
        self.assertTrue(os.path.exists('Methane Plot.png'), "Failed to save the plot.")
        
        
if __name__ == '__main__':
    unittest.main()