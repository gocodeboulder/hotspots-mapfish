# -*- coding: utf-8 -*-

from hotspots.tests import *

class TestUsersController(TestController):
    def test_index(self):
        response = self.app.get(url(controller='users'))
        # Test response...
