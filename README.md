HOTSPOTS
==========

Using the [mapfish](http://www.mapfish.org) framework

[![Stories in Ready](https://badge.waffle.io/gocodeboulder/business-site-location.png?label=ready&title=Ready)](http://waffle.io/gocodeboulder/business-site-location)

To test:
---------

1. Install Python 2, python setup tools, and virtualenv.

2. Create a virtual env. This creates a python environment in the mapfishenv folder in your home directory.

```bash
virtualenv create --no-site-packages ~/mapfishenv
```

3. Activate your virtualenv.

```bash
. ~/mapfishenv/bin/activate
```

4. Clone the repository and initialize your development environment.

```bash
git clone git@github.com:gocodeboulder/hotspots-mapfish.git
cd hotspots-mapfish
python setup.py develop
```

5. Start the development server. Listens on port 5000

```bash
paster serve --reload development.ini
```

**Note:** You have to have the virtualenv activated for the paster script to work. The virtualenv stores all your Python libraries necessary for the app to work.

Check out the [Mapfish documentation](http://mapfish.org/doc/2.2/index.html) and [Pylons documentation](http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/).

Why:
----

This is meant to be a back end for whatever front end we come up with. We can use whatever front end. It comes by default with the ExtJS, OpenLayers, GeoExt JavaScript libraries. 
