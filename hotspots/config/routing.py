"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    # CUSTOM ROUTES HERE
    map.connect("/census/count", controller="census", action="count")
    map.resource("census", "census")
    
    map.connect("/broadband_speeds/count", controller="broadband_speeds", action="count")
    map.resource("broadband_speed", "broadband_speeds")

    map.connect("/zones/count", controller="zones", action="count")
    map.resource("zone", "zones")

    #map.resource("user", "users")
    #map.connect("/users/count", controller="users", action="count")

    map.connect("/cellulars/count", controller="cellulars", action="count")
    map.resource("cellular", "cellulars")

    map.connect("/parking_facilities/count", controller="parking_facilities", action="count")
    map.resource("parking_facility", "parking_facilities")

    map.connect("/parking_meters/count", controller="parking_meters", action="count")
    map.resource("parking_meter", "parking_meters")

    return map
