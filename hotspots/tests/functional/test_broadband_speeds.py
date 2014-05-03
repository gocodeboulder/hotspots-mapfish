# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestBroadbandSpeedsController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='broadband_speeds'))
        # Test response...
