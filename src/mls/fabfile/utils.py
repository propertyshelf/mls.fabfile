# -*- coding: utf-8 -*-
"""Various utility functions."""

from chef import autoconfigure, Search
from fabric import api


def mls_config():
    """Get the MLS configuration object for the current node."""
    chef_api = autoconfigure()
    if '127.0.0.1:2222' in api.env.hosts:
        query = 'hostname:%s' % api.env.hostname
    else:
        query = 'ipaddress:%s' % api.env.host
    for node in Search('node', query, api=chef_api):
        try:
            return node.object['mls']
        except KeyError:
            return {}
