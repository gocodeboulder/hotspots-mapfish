# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestZonesController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='zones'))
        # Test response...
