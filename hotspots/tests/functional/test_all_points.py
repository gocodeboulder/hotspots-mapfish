from hotspots.tests import *

class TestAllPointsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='all_points', action='index'))
        # Test response...
