# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestCellularController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='cellular'))
        # Test response...
