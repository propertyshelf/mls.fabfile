# -*- coding: utf-8 -*-
"""Manage MLS application client components."""

from fabric.api import task


@task
def remove():
    """Remove an existing MLS application client."""


@task
def update():
    """Update the client packages."""


@task
def restart():
    """Restart the application client component."""
