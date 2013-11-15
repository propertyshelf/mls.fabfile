# -*- coding: utf-8 -*-
"""Manage MLS application client components."""

from fabric import api


@api.task
def remove():
    """Remove an existing MLS application client."""


@api.task
@api.roles('worker')
def update():
    """Update the client packages."""


@api.task
@api.roles('worker')
def restart():
    """Restart the application client component."""
