# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestCountriesController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='countries'))
        # Test response...
