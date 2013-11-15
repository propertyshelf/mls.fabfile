# -*- coding: utf-8 -*-
"""Sample MLS deployment script."""

from fabric import api

from mls.fabfile import *
from mls.fabfile.environments import *


api.env.role_database = 'mls_db'
api.env.role_frontend = 'mls_fe'
api.env.role_staging = 'mls_staging'
api.env.role_worker = 'mls_app'

api.env.flavor_database = '5'
api.env.flavor_frontend = '2'
api.env.flavor_staging = '2'
api.env.flavor_worker = '3'

api.env.nodename_database = 'mls-db'
api.env.nodename_frontend = 'mls-fe'
api.env.nodename_staging = 'mls-staging'
api.env.nodename_worker = 'mls-app'

api.env.os_image = '92a28e50-181d-4fc7-a071-567d26fc95f6'
