# -*- coding: utf-8 -*-
"""Bootstrap new servers."""

from fabric import api
from mls.fabfile import rackspace
from mls.fabfile.exceptions import err


@api.task
def database(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone database server."""
    nodename = nodename or api.env.get('nodename_database')
    nodename = nodename or err(
        'The definition for "nodename_database" is missing!'
    )

    image = image or api.env.get('os_image')
    image = image or err('The definition for "os_image" is missing!')

    flavor = flavor or api.env.get('flavor_database')
    flavor = flavor or err('The definition for "flavor_database" is missing!')

    role = api.env.get('role_database')
    role = role or err('The definition for "role_database" is missing!')

    runlist = ','.join([
        'role[%s]' % role,
        'recipe[propertyshelf::rackspace_backup]',
    ])

    opts = dict(
        environment='production',
        flavor=flavor,
        image=image,
        nodename=nodename,
        runlist=runlist,
        servername=nodename,
    )
    rackspace.create(**opts)


@api.task
def frontend(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone frontend server."""
    nodename = nodename or api.env.get('nodename_frontend')
    nodename = nodename or err(
        'The definition for "nodename_frontend" is missing!'
    )

    image = image or api.env.get('os_image')
    image = image or err('The definition for "os_image" is missing!')

    flavor = flavor or api.env.get('flavor_database')
    flavor = flavor or err('The definition for "flavor_database" is missing!')

    role = api.env.get('role_frontend')
    role = role or err('The definition for "role_frontend" is missing!')

    runlist = ','.join([
        'role[%s]' % role,
    ])

    opts = dict(
        environment='production',
        flavor=flavor,
        image=image,
        nodename=nodename,
        runlist=runlist,
        servername=nodename,
    )
    rackspace.create(**opts)


@api.task
def worker(nodename=None, image=None, flavor=None):
    """Bootstrap a new standalone application worker."""
    number = rackspace.next_client_number(
        environment='production',
        rolename=api.env.role_worker,
    )

    nodename = nodename or api.env.get('nodename_worker') + '-%02d' % number
    nodename = nodename or err(
        'The definition for "nodename_worker" is missing!'
    )

    image = image or api.env.get('os_image')
    image = image or err('The definition for "os_image" is missing!')

    flavor = flavor or api.env.get('flavor_worker')
    flavor = flavor or err('The definition for "flavor_worker" is missing!')

    role = api.env.get('role_worker')
    role = role or err('The definition for "role_worker" is missing!')

    runlist = ','.join([
        'role[%s]' % role,
    ])

    opts = dict(
        environment='production',
        flavor=flavor,
        image=image,
        nodename=nodename,
        runlist=runlist,
        servername=nodename,
    )
    rackspace.create(**opts)


@api.task
def bundle_db_fe_app(nodename=None, image=None, flavor=None):
    """Bootstrap a new MLS bundle: Database, Frontend, App Worker."""
    nodename = nodename or api.env.get('nodename_database')
    nodename = nodename or err(
        'The definition for "nodename_database" is missing!'
    )

    image = image or api.env.get('os_image')
    image = image or err('The definition for "os_image" is missing!')

    flavor = flavor or api.env.get('flavor_database')
    flavor = flavor or err('The definition for "flavor_database" is missing!')

    role_database = api.env.get('role_database')
    role_database = role_database or err('The definition for "role_database" is missing!')
    role_frontend = api.env.get('role_frontend')
    role_frontend = role_frontend or err('The definition for "role_frontend" is missing!')
    role_worker = api.env.get('role_worker')
    role_worker = role_worker or err('The definition for "role_worker" is missing!')

    runlist = ','.join([
        'role[%s]' % role_database,
        'role[%s]' % role_frontend,
        'role[%s]' % role_worker,
        'recipe[propertyshelf::rackspace_backup]',
    ])

    opts = dict(
        environment='production',
        flavor=flavor,
        image=image,
        nodename=nodename,
        runlist=runlist,
        servername=nodename,
    )
    rackspace.create(**opts)


@api.task
def staging(nodename=None, image=None, flavor=None):
    """Bootstrap a staging system."""
    nodename = nodename or api.env.get('nodename_staging')
    nodename = nodename or err(
        'The definition for "nodename_staging" is missing!'
    )

    image = image or api.env.get('os_image')
    image = image or err('The definition for "os_image" is missing!')

    flavor = flavor or api.env.get('flavor_database')
    flavor = flavor or err('The definition for "flavor_database" is missing!')

    role = api.env.get('role_staging')
    role = role or err('The definition for "role_staging" is missing!')

    runlist = ','.join([
        'role[%s]' % role,
    ])

    opts = dict(
        environment='staging',
        flavor=flavor,
        image=image,
        nodename=nodename,
        runlist=runlist,
        servername=nodename,
    )
    rackspace.create(**opts)
