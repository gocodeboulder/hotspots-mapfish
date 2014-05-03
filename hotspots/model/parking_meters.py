# -*- coding: utf-8 -*-

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, MultiPolygon

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base

class ParkingMeter(Base, GeometryTableMixIn):
    __tablename__ = 'parking_meters'
    __table_args__ = {
        "autoload": True,
        "autoload_with": Session.bind
    }
    geom = GeometryColumn(MultiPolygon(srid=4326))
