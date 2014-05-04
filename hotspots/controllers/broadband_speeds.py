# -*- coding: utf-8 -*-

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect

from hotspots.lib.base import BaseController
from hotspots.model.broadband_speeds import BroadbandSpeed
from hotspots.model.zones import Zone
from hotspots.model.meta import Session

from mapfish.protocol import Protocol, create_default_filter
from mapfish.decorators import geojsonify
from sqlalchemy import and_
from geoalchemy.functions import functions

class BroadbandSpeedsController(BaseController):
    readonly = False # if set to True, only GET is supported

    def __init__(self):
        self.protocol = Protocol(Session, BroadbandSpeed, self.readonly)

    @geojsonify
    def index(self, format='json'):
        """GET /: return all features."""
        # If no filter argument is passed to the protocol index method
        # then the default MapFish filter is used.
        #
        # If you need your own filter with application-specific params 
        # taken into acount, create your own filter and pass it to the
        # protocol read method.
        #
        # E.g.
        #
        # from sqlalchemy.sql import and_
        #
        # default_filter = create_default_filter(request, BroadbandSpeed)
        # filter = and_(default_filter, BroadbandSpeed.columname.ilike('%value%'))
        # return self.protocol.read(request, filter=filter)
        default_filter = create_default_filter(request, BroadbandSpeed)

        if "zones_f" in request.params:
            #zones will be a javascript list
            zones_q = request.params["zones_f"].split(",")
            #zones = Session.query(functions.geometry_type(functions.collect(Zone.geom))).filter(and_(Zone.zone_general.in_(zones_q),
            #                                                                                       Zone.geom != None)).scalar()
            zones = Session.query(functions.union(Zone.geom)).filter(Zone.zone_general.in_(zones_q)).first()
            filter = and_(default_filter, BroadbandSpeed.geom.within(zones))
        else:
            filter = default_filter

        if format != 'json':
            abort(404)
        return self.protocol.read(request, filter=filter)

    @geojsonify
    def show(self, id, format='json'):
        """GET /id: Show a specific feature."""
        if format != 'json':
            abort(404)
        return self.protocol.read(request, response, id=id)

    #@geojsonify
    #def create(self):
    #    """POST /: Create a new feature."""
    #    return self.protocol.create(request, response)
    #
    #@geojsonify
    #def update(self, id):
    #    """PUT /id: Update an existing feature."""
    #    return self.protocol.update(request, response, id)
    #
    #def delete(self, id):
    #    """DELETE /id: Delete an existing feature."""
    #    return self.protocol.delete(request, response, id)

    def count(self):
        """GET /count: Count all features."""
        return self.protocol.count(request)
