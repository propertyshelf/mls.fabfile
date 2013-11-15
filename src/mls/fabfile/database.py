# -*- coding: utf-8 -*-
"""Manage MLS database components."""

from fabric import api


@api.task
def restart():
    """Restart the database component."""


@api.task
def download_data():
    """Download the database files from the server."""


@api.task
def download_zodb():
    """Download ZODB part of Zope's data from the server."""


@api.task
def download_blobs():
    """Download blob part of Zope's data from the server."""


@api.task
def upload_data():
    """Upload the database files to the server."""


@api.task
def upload_zodb():
    """Upload ZODB part of Zope's data to the server."""


@api.task
def upload_blob():
    """Upload blob part of Zope's data to the server."""


@api.task
def backup():
    """Perform a backup of Zope's data on the server."""


@api.task
def restore():
    """Restore an existing backup of Zope's data on the server."""
