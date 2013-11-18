# -*- coding: utf-8 -*-

from fabric import api


def err(msg):
    return api.abort(msg)
