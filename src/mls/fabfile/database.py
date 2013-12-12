# -*- coding: utf-8 -*-
"""Manage MLS database components."""

from fabric import api
from mls.fabfile.utils import mls_config
from propertyshelf.fabfile.common import zodb


@api.task
@api.roles('database')
def restart():
    """Restart the database component."""
    zodb.restart(service='zeoserver')


@api.task
@api.roles('database')
def download_data():
    """Download the database files from the server."""
    zodb.download_data(mls_config)


@api.task
@api.roles('database')
def download_zodb():
    """Download ZODB part of Zope's data from the server."""
    zodb.download_zodb(mls_config)


@api.task
@api.roles('database')
def download_blobs():
    """Download blob part of Zope's data from the server."""
    zodb.download_blobs(mls_config)


@api.task
@api.roles('database')
def upload_data():
    """Upload the database files to the server."""
    zodb.upload_data(mls_config)


@api.task
@api.roles('database')
def upload_zodb(start_when_done=True):
    """Upload ZODB part of Zope's data to the server."""
    zodb.upload_zodb(mls_config)


@api.task
@api.roles('database')
def upload_blob(start_when_done=True):
    """Upload blob part of Zope's data to the server."""
    zodb.upload_blob(mls_config)
