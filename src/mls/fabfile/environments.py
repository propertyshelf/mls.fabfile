# -*- coding: utf-8 -*-
"""Environment definitions."""

from chef.fabric import chef_roledefs
from fabric import api


@api.task
def development():
    """Work locally with vagrant."""
    # Change the default user to 'vagrant'.
    result = api.local('vagrant ssh-config | grep IdentityFile', capture=True)
    api.env.key_filename = result.replace('"', '').split()[1]
    api.env.user = 'vagrant'

    # Connect to the port-forwarded ssh.
    api.env.hosts = ['127.0.0.1:2222']

    # Set role definitions for vagrant.
    api.env.roledefs = {
        api.env.get('ROLE_APP', 'mls_app'): ['127.0.0.1:2222', ],
        api.env.get('ROLE_LBL', 'mls_load'): ['127.0.0.1:2222', ],
        api.env.get('ROLE_ZEO', 'mls_zeo'): ['127.0.0.1:2222', ],
    }


@api.task
def staging():
    """Work with the staging environment."""
    api.env.roledefs = chef_roledefs(
        hostname_attr=['ipaddress'],
        environment='staging',
    )


@api.task
def production():
    """Work with the production environment."""
    api.env.roledefs = chef_roledefs(
        hostname_attr=['ipaddress'],
        environment='production',
    )
