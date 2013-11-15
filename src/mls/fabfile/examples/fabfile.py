# -*- coding: utf-8 -*-
"""Sample MLS deployment script."""

from fabric import api

from mls.fabfile import *
from mls.fabfile.environments import *


api.env.role_database = 'mls_db'
api.env.role_frontend = 'mls_fe'
api.env.role_staging = 'mls_staging'
api.env.role_worker = 'mls_app'
