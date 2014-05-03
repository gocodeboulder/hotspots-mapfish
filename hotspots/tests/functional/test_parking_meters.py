# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestParkingMetersController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='parking_meters'))
        # Test response...
