# -*- coding: utf-8 -*-

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, Point

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base

class Cellular(Base, GeometryTableMixIn):
    __tablename__ = 'cellular_performance'
    __table_args__ = {
        "schema": 'public',
        "autoload": True,
        "autoload_with": Session.bind
    }
    location = GeometryColumn(Point(srid=4326))
