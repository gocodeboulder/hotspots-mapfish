# -*- coding: utf-8 -*-

from sqlalchemy import Column, types

from geoalchemy import GeometryColumn, MultiPolygon

from mapfish.sqlalchemygeom import GeometryTableMixIn
from hotspots.model.meta import Session, Base
from sqlalchemy import and_, or_
from geoalchemy.functions import functions

class Zone(Base, GeometryTableMixIn):
    __tablename__ = 'zoning'
    __table_args__ = {
        "autoload": True,
        "autoload_with": Session.bind
    }
    geom = GeometryColumn(MultiPolygon(srid=4326))
