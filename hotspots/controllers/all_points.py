import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from hotspots.lib.base import BaseController, render
from mapfish.decorators import geojsonify

from hotspots import model
from hotspots.model.meta import Session

log = logging.getLogger(__name__)

class AllPointsController(BaseController):
    """Want to accept a list of zone codes and return all interesting points within those zones
       Maybe too to accept census filter criteria and return points matching (actually, do we need this?)
    """
    @geojsonify
    def index(self):
        # Return a rendered template
        #return render('/all_points.mako')
        # or, return a string
        return 'Hello World'
