# -*- coding: utf-8 -*-
"""Manage MLS frontend components like web server, load balancer and cache."""

from fabric import api


@api.task
@api.roles('frontend')
def restart():
    """Restart the frontend components."""


@api.task
@api.roles('frontend')
def restart_nginx():
    """Restart the NginX web server component."""


@api.task
@api.roles('frontend')
def restart_varnish():
    """Restart the Varnish caching proxy component."""


@api.task
@api.roles('frontend')
def restart_haproxy():
    """Restart the HA-Proxy load balancer component."""
