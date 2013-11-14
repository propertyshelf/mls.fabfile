# -*- coding: utf-8 -*-
"""Manage MLS database components."""

from fabric.api import task


@task
def restart():
    """Restart the database component."""


@task
def download_data():
    """Download the database files from the server."""


@task
def download_zodb():
    """Download ZODB part of Zope's data from the server."""


@task
def download_blobs():
    """Download blob part of Zope's data from the server."""


@task
def upload_data():
    """Upload the database files to the server."""


@task
def upload_zodb():
    """Upload ZODB part of Zope's data to the server."""


@task
def upload_blob():
    """Upload blob part of Zope's data to the server."""


@task
def backup():
    """Perform a backup of Zope's data on the server."""


@task
def restore():
    """Restore an existing backup of Zope's data on the server."""
