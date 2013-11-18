# -*- coding: utf-8 -*-
"""Manage MLS database components."""

from fabric import api


@api.task
@api.roles('database')
def restart():
    """Restart the database component."""
    raise NotImplementedError


@api.task
@api.roles('database')
def download_data():
    """Download the database files from the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def download_zodb():
    """Download ZODB part of Zope's data from the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def download_blobs():
    """Download blob part of Zope's data from the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def upload_data():
    """Upload the database files to the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def upload_zodb():
    """Upload ZODB part of Zope's data to the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def upload_blob():
    """Upload blob part of Zope's data to the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def backup():
    """Perform a backup of Zope's data on the server."""
    raise NotImplementedError


@api.task
@api.roles('database')
def restore():
    """Restore an existing backup of Zope's data on the server."""
    raise NotImplementedError
