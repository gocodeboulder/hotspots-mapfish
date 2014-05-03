# -*- coding: utf-8 -*-

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, Point

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base

class BroadbandSpeed(Base, GeometryTableMixIn):
    __tablename__ = 'broadband_speeds'
    __table_args__ = {
        "schema": 'public',
        "autoload": True,
        "autoload_with": Session.bind
    }
    geom = GeometryColumn(Point(srid=4326))
