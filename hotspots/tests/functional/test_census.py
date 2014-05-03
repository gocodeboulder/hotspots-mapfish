# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestCensusController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='census'))
        # Test response...
