# -*- coding: utf-8 -*-
"""Manage MLS application client components."""

from fabric import api
from mls.fabfile import utils


@api.task
def remove():
    """Remove an existing MLS application client."""
    raise NotImplementedError


@api.task
@api.roles('worker')
def update():
    """Update the client packages."""
    utils.supervisorctl(command='stop', service='application')
    utils.backup_dev_packages()
    utils.run_buildout()
    utils.supervisorctl(command='start', service='application')


@api.task
@api.roles('worker')
def restart():
    """Restart the application client component."""
    utils.supervisorctl(command='restart', service='application')
