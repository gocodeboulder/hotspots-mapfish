# -*- coding: utf-8 -*-

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, MultiPolygon

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base

class Census(Base, GeometryTableMixIn):
    __tablename__ = 'census'
    __table_args__ = {
        "schema": 'public',
        "autoload": True,
        "autoload_with": Session.bind
    }
    geom = GeometryColumn(MultiPolygon(srid=4326))
