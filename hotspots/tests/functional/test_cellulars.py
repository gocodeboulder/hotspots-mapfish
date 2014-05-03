# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestCellularsController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='cellulars'))
        # Test response...
