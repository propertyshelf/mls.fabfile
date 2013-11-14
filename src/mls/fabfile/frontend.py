# -*- coding: utf-8 -*-
"""Manage MLS frontend components like web server, load balancer and cache."""

from fabric.api import task


@task
def restart():
    """Restart the frontend components."""


@task
def restart_nginx():
    """Restart the NginX web server component."""


@task
def restart_varnish():
    """Restart the Varnish caching proxy component."""


@task
def restart_haproxy():
    """Restart the HA-Proxy load balancer component."""
