# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestParkingFacilitiesController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='parking_facilities'))
        # Test response...
