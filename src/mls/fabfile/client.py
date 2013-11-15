# -*- coding: utf-8 -*-
"""Manage MLS application client components."""

from fabric import api


@api.task
def remove():
    """Remove an existing MLS application client."""


@api.task
def update():
    """Update the client packages."""


@api.task
def restart():
    """Restart the application client component."""
