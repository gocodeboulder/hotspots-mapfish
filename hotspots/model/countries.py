# -*- coding: utf-8 -*-

from sqlalchemy import Column, types, Integer

from geoalchemy import GeometryColumn, MultiPolygon

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base

class Country(Base, GeometryTableMixIn):
    __tablename__ = 'countries'
    __table_args__ = {
        "autoload": True,
        "autoload_with": Session.bind
    }
    #the_geom = GeometryColumn(MultiPolygon(srid=4326))
    gid = Column(Integer, primary_key=True)
    geom = GeometryColumn(MultiPolygon(srid=4326))
