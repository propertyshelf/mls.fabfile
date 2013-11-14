# -*- coding: utf-8 -*-
"""Bootstrap new servers."""

from fabric import api


@api.task
def base():
    """Bootstrap a new MLS base system.

    The base system contains:
    - Frontend components: NginX, Varnish, HA-Proxy
    - Application clients
    - A ZEO server.
    """


@api.task
def client():
    """Bootstrap a new application client."""


@api.task
def staging():
    """Bootstrap a staging system."""
