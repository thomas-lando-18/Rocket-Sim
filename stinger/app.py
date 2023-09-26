from flask import Flask

# Import Endpoints
from endpoints.admin import admin_endpoints
from endpoints.location import location_endpoints
from endpoints.rocket import rocket_endpoints
from endpoints.satellite import satellite_endpoints


stinger = Flask("__name__")

# Admin/ General endpoints
stinger.register_blueprint(admin_endpoints)

# Location Endpoints
stinger.register_blueprint(location_endpoints)

# Satellite Endpoints
stinger.register_blueprint(satellite_endpoints)

# Rocket Enpdoints
stinger.register_blueprint(rocket_endpoints)

