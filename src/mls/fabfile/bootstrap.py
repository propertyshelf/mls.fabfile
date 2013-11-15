# -*- coding: utf-8 -*-
"""Bootstrap new servers."""

from fabric import api
from mls.fabfile import rackspace


@api.task
def database(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone database server."""
    name = nodename
    name = name or api.env.get('nodename_database')
    name = name or 'mls-zeo'

    runlist = ','.join([
        'role[%s]' % api.env.role_database or 'mls_zeo',
        'recipe[propertyshelf::rackspace_backup]',
    ])

    opts = dict(
        environment='production',
        flavor=flavor or api.env.get('flavor_database') or '5',
        image=image or api.env.get('os_image'),
        nodename=name,
        runlist=runlist,
        servername=name,
    )
    rackspace.create(**opts)


@api.task
def frontend(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone frontend server."""
    name = nodename
    name = name or api.env.get('nodename_frontend')
    name = name or 'mls-lbl'

    opts = dict(
        environment='production',
        flavor=flavor or api.env.get('flavor_frontent') or '2',
        image=image or api.env.get('os_image'),
        nodename=name,
        runlist='role[%s]' % api.env.role_frontend or 'mls_lbl',
        servername=name,
    )
    rackspace.create(**opts)


@api.task
def worker(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone application worker."""
    number = rackspace.next_client_number(
        environment='production',
        rolename=api.env.role_worker,
    )

    name = nodename
    name = name or api.env.get('nodename_worker') + '-%02d' % number
    name = name or 'mls-lbl'

    opts = dict(
        environment='production',
        flavor=flavor or api.env.get('flavor_worker') or '2',
        image=image or api.env.get('os_image'),
        nodename=name,
        runlist='role[%s]' % api.env.role_worker or 'mls_app',
        servername=name,
    )
    rackspace.create(**opts)


@api.task
def base(nodename=None, image=None, flavor=None):
    """Bootstrap a new MLS base system.

    The base system contains:
    - Frontend server components
    - Application clients
    - Database server components.
    """
    name = nodename
    name = name or api.env.get('nodename_database')
    name = name or 'mls-zeo'

    runlist = ','.join([
        'role[%s]' % api.env.role_database or 'mls_zeo',
        'role[%s]' % api.env.role_frontend or 'mls_lbl',
        'role[%s]' % api.env.role_worker or 'mls_app',
        'recipe[propertyshelf::rackspace_backup]',
    ])

    opts = dict(
        environment='production',
        flavor=flavor or api.env.get('flavor_database') or '5',
        image=image or api.env.get('os_image'),
        nodename=name,
        runlist=runlist,
        servername=name,
    )
    rackspace.create(**opts)


@api.task
def staging(nodename=None, image=None, flavor=None):
    """Bootstrap a staging system."""
    name = nodename
    name = name or api.env.get('nodename_staging')
    name = name or 'mls-staging'

    opts = dict(
        environment='staging',
        flavor=flavor or api.env.get('flavor_staging') or '2',
        image=image or api.env.get('os_image'),
        nodename=name,
        runlist='role[%s]' % api.env.role_staging or 'mls_staging',
        servername=name,
    )
    rackspace.create(**opts)
