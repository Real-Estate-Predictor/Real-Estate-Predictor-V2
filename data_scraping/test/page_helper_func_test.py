

import sys
import os
sys.path.append("../")
# 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from data_scraping.helperFunc.pageHelperFunc import pageUtils

import unittest
# from bs4 import BeautifulSoup

class TestPageUtils(unittest.TestCase):

    def test_isNextPageAvailable_true(self):
        # Initialize the pageUtils class
        page_utils = pageUtils()

        # Read the HTML file from the same directory
        with open('./page_with_next_button.html', 'r', encoding='utf-8') as file:
            html_source_with_next_button = file.read()

        # Call the isNextPageAvailable function with the HTML content
        result_next_button = page_utils.isNextPageAvailable(html_source_with_next_button)

        # Check if the result is True or False based on the expected output
        self.assertTrue(result_next_button, "Next page button is available")


    def test_isNextPageAvailable_false(self):
        # Initialize the pageUtils class
        page_utils = pageUtils()
        
        # Read the HTML file from the same directory
        with open('./page_with_no_next_button.html', 'r', encoding='utf-8') as file:
            html_source_no_next_button = file.read()

        result_no_next_button = page_utils.isNextPageAvailable(html_source_no_next_button)

        # If the expected output is False, use the following assert instead:
        self.assertFalse(result_no_next_button, "Next page button is not available") 


if __name__ == '__main__':
    unittest.main()
