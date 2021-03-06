# -*- mode: python; fill-column: 100; comment-column: 100; -*-

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import base_test


class ElementLocationTest(base_test.WebDriverBaseTest):

    def test_find_element_by_id(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_id("id")
        self.assertEquals("id", e.text)

    def test_find_element_by_name(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_name("name")
        self.assertEquals("name", e.text)

    def test_find_element_by_css_selector(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_css_selector("#id")
        self.assertEquals("id", e.text)

    def test_find_element_by_link_text(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_link_text("link text")
        self.assertEquals("link text", e.text)

    def test_find_element_by_partial_link_text(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_partial_link_text("link tex")
        self.assertEquals("link text", e.text)

    def test_find_element_by_xpath(self):
        self.driver.get(self.webserver.where_is("element_location/elements.html"))
        e = self.driver.find_element_by_xpath("//*[@id='id']")
        self.assertEquals("id", e.text)

if __name__ == "__main__":
    unittest.main()
