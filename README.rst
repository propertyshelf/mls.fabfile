mls.fabfile
===========

This project contains a bunch of fabric commands we use at `Propertyshelf`_
to deploy and maintain our MLS systems.


Requirements
------------

`mls.fabfile` currently uses `knife`_ to communicate with Rackspace servers.
Please make sure `knife` is installed and configured successfully on your
system.


Install
-------

You can install `mls.fabfile` with PIP::

    pip install mls.fabfile

All required dependencies will be installed automatically.


Usage
-----

First, we need a working `knife.rb` file to interact with our Chef server and
the Rackspace cloud eco system. Below is an example `knife.rb` file that gets
all its required info from environment variables. This way you can add this
`knife.rb` file inside a `.chef` directory to your project and savely put it
under version control::

    # Logging.
    log_level                         :info
    log_location                      STDOUT

    # Chef server configuration.
    chef_server_url                   "#{ENV['KNIFE_CHEF_SERVER']}"
    client_key                        "#{ENV['KNIFE_CLIENT_KEY']}"
    node_name                         "#{ENV['KNIFE_NODE_NAME']}"
    validation_client_name            "#{ENV['KNIFE_VALIDATION_CLIENT_NAME']}"
    validation_key                    "#{ENV['KNIFE_VALIDATION_CLIENT_KEY']}"
    encrypted_data_bag_secret         "#{ENV['ENCRYPTED_DATA_BAG_SECRET_FILE']}"

    # Rackspace API configuration.
    knife[:rackspace_api_key]       = "#{ENV['RACKSPACE_API_KEY']}"
    knife[:rackspace_api_username]  = "#{ENV['RACKSPACE_USERNAME']}"
    knife[:rackspace_endpoint]      = "#{ENV['RACKSPACE_ENDPOINT']}"
    knife[:rackspace_version]       = "#{ENV['RACKSPACE_VERSION']}"


Next, we need a `fabfile.py`. All we need to do is to import `mls.fabfile`
to make the fabric commands available and the available environments we can
work with from `propertyshelf.fabfile.common`.::

    # -*- coding: utf-8 -*-
    """Sample MLS deployment script."""

    from fabric import api

    from mls.fabfile import *
    from propertyshelf.fabfile.common.environments import *


    # Definition of role names to be used.
    api.env.role_database = 'mls_db'
    api.env.role_frontend = 'mls_fe'
    api.env.role_staging = 'mls_staging'
    api.env.role_worker = 'mls_app'

    # Definition of used Rackspace flavors (server sized) for our servers.
    api.env.flavor_database = '5'
    api.env.flavor_frontend = '2'
    api.env.flavor_staging = '2'
    api.env.flavor_worker = '3'

    # Definition of node names to be used.
    api.env.nodename_database = 'mls-db'
    api.env.nodename_frontend = 'mls-fe'
    api.env.nodename_staging = 'mls-staging'
    api.env.nodename_worker = 'mls-app'

    # The Rackspace server image we use. This is a Debian 6.0.6.
    api.env.os_image = '92a28e50-181d-4fc7-a071-567d26fc95f6'

    # MLS specific configuration.
    api.env.domain = 'mls-example.com'
    api.env.mls_customizations = ['mlsext.realtorcom', ]
    api.env.mls_policy_enabled = True
    api.env.mls_policy_package = 'mlspolicy.example'
    api.env.mls_policy_package_url = 'git https://github.com/yourname/mlspolicy.example'

You can now use fabric to manage your MLS::

    $ fab -l
    Sample MLS deployment script.

    Available commands:

        development                 Work locally with vagrant.
        production                  Work with the production environment.
        staging                     Work with the staging environment.
        bootstrap.bundle_db_fe_app  Bootstrap a new MLS bundle: Database, Frontend, App Worker.
        bootstrap.database          Bootstrap a new standalone database server.
        bootstrap.frontend          Bootstrap a new standalone frontend server.
        bootstrap.staging           Bootstrap a staging system.
        bootstrap.worker            Bootstrap a new standalone application worker.
        client.remove               Remove an existing MLS application client.
        client.restart              Restart the application client component.
        client.update               Update the client packages.
        database.backup             Perform a backup of Zope's data on the server.
        database.download_blobs     Download blob part of Zope's data from the server.
        database.download_data      Download the database files from the server.
        database.download_zodb      Download ZODB part of Zope's data from the server.
        database.restart            Restart the database component.
        database.restore            Restore an existing backup of Zope's data on the server.
        database.upload_blob        Upload blob part of Zope's data to the server.
        database.upload_data        Upload the database files to the server.
        database.upload_zodb        Upload ZODB part of Zope's data to the server.
        frontend.restart            Restart the frontend components.
        frontend.restart_haproxy    Restart the HA-Proxy load balancer component.
        frontend.restart_nginx      Restart the NginX web server component.
        frontend.restart_varnish    Restart the Varnish caching proxy component.
        roles.check                 Check if the required roles are available.
        roles.create_missing        Create missing roles on the chef server.

Before we can start it is a good idea to check if all roles we defined are
available on the chef server::

    $ fab roles.check
    Role mls_fe NOT available.
    Role mls_db NOT available.
    Role mls_staging NOT available.
    Role mls_app NOT available.

    Done.

To create the missing roles based on our configuration, we simply have to do::

    $ fab roles.create_missing
    Created role mls_db
    Created role mls_fe
    Created role mls_app
    Created role mls_staging

    Done.

Now we can create our staging system::

    $ fab bootstrap.staging
    [localhost] local: knife rackspace server create -S mls-staging -N mls-staging -f 5 -I 92a28e50-181d-4fc7-a071-567d26fc95f6 -r role[rackspace],role[mls_staging] -E staging

    ...

    Done.

Note that there can only be one staging system. If you try to add another one
with the same name, you'll get an error message::

    $ fab bootstrap.staging

    Fatal error: Server "mls-staging" already exists in environment "staging".

    Aborting.

If you need a second one, you can adjust the node name manually::

    $ fab bootstrap.staging:nodename=mls-staging2
    [localhost] local: knife rackspace server create -S mls-staging2 -N mls-staging2 -f 5 -I 92a28e50-181d-4fc7-a071-567d26fc95f6 -r role[rackspace],role[mls_ni_staging] -E staging

    ...

    Done.

You can now manage the single components::

    $ fab staging frontend.restart
    [x.x.x.x] Executing task 'frontend.restart'
    [x.x.x.x] sudo: /etc/init.d/haproxy restart
    [x.x.x.x] out: sudo password:

    [x.x.x.x] out: Restarting haproxy: haproxy.
    [x.x.x.x] out:

    [x.x.x.x] sudo: /etc/init.d/varnish restart
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out: Stopping HTTP accelerator: varnishd.
    [x.x.x.x] out: Starting HTTP accelerator: varnishd.
    [x.x.x.x] out:

    [x.x.x.x] sudo: /etc/init.d/nginx restart
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out: Restarting nginx: nginx.
    [x.x.x.x] out:


    Done.
    Disconnecting from x.x.x.x... done.

We also support download of the database files for local testing::

    $ fab production database.download_data
    [x.x.x.x] Executing task 'database.download_data'
    This will overwrite your local Data.fs. Are you sure you want to continue? [Y/n]
    [localhost] local: mkdir -p var/filestorage
    [localhost] local: mv var/filestorage/Data.fs var/filestorage/Data.fs.bak
    [x.x.x.x] out: sudo password:
    [x.x.x.x] sudo: rsync -a var/filestorage/Data.fs /tmp/Data.fs
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out:
    [x.x.x.x] download: /Volumes/Work/Propertyshelf/MLS/Provisioning/var/filestorage/Data.fs <- /tmp/Data.fs
    This will overwrite your local blob files. Are you sure you want to continue? [Y/n]
    [localhost] local: rm -rf var/blobstorage_bak
    [localhost] local: mv var/blobstorage var/blobstorage_bak
    [x.x.x.x] sudo: rsync -a ./var/blobstorage /tmp/
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out:
    [x.x.x.x] sudo: tar czf blobstorage.tgz blobstorage
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out:
    [x.x.x.x] download: /Volumes/Work/Propertyshelf/MLS/Provisioning/var/blobstorage.tgz <- /tmp/blobstorage.tgz

    Warning: Local file /Volumes/Work/Propertyshelf/MLS/Provisioning/var/blobstorage.tgz already exists and is being overwritten.

    [localhost] local: tar xzf blobstorage.tgz

    Done.
    Disconnecting from x.x.x.x... done.

Once we have local data files, we can upload them to our development environment
(a vagrant VM)::

    $ fab development database.upload_data client.restart
    [localhost] local: vagrant ssh-config | grep IdentityFile
    [127.0.0.1:2222] Executing task 'database.upload_data'
    This will overwrite your remote Data.fs. Are you sure you want to continue? [y/N] y
    [127.0.0.1:2222] sudo: mkdir -p /tmp/upload
    [127.0.0.1:2222] put: var/filestorage/Data.fs -> /tmp/upload/Data.fs
    [127.0.0.1:2222] sudo: chown mls /tmp/upload/Data.fs
    [127.0.0.1:2222] sudo: supervisorctl stop zeoserver
    [127.0.0.1:2222] out: zeoserver: stopped
    [127.0.0.1:2222] out:

    [127.0.0.1:2222] sudo: mv var/filestorage/Data.fs var/filestorage/Data.fs.bak
    [127.0.0.1:2222] sudo: mv /tmp/upload/Data.fs var/filestorage/Data.fs
    This will overwrite your remote blob files. Are you sure you want to continue? [y/N] y
    [127.0.0.1:2222] sudo: mkdir -p /tmp/upload
    [localhost] local: tar czf blobstorage_upload.tgz blobstorage
    [127.0.0.1:2222] put: var/blobstorage_upload.tgz -> /tmp/upload/blobstorage.tgz
    [127.0.0.1:2222] sudo: chown mls /tmp/upload/blobstorage.tgz
    [127.0.0.1:2222] sudo: tar xzf blobstorage.tgz
    [127.0.0.1:2222] sudo: supervisorctl stop zeoserver
    [127.0.0.1:2222] out: zeoserver: ERROR (not running)
    [127.0.0.1:2222] out:

    [127.0.0.1:2222] sudo: mv var/blobstorage var/blobstorage_bak
    [127.0.0.1:2222] sudo: mv /tmp/upload/blobstorage var
    [127.0.0.1:2222] sudo: supervisorctl start zeoserver
    [127.0.0.1:2222] out: zeoserver: started
    [127.0.0.1:2222] out:

    [127.0.0.1:2222] Executing task 'client.restart'
    [127.0.0.1:2222] sudo: supervisorctl restart application
    [127.0.0.1:2222] out: application: stopped
    [127.0.0.1:2222] out: application: started
    [127.0.0.1:2222] out:


    Done.
    Disconnecting from 127.0.0.1:2222... done.

We can also get a list of nodes for already defined roles::

    $ fab roles.list_nodes
    Role: mls_fe
    - mls-fe: x.x.x.x

    Role: mls_db
    - mls-db: x.x.x.x

    Role: mls_staging
    - mls-staging: x.x.x.x
    - vagrant-mls-staging: 10.0.2.15

    Role: mls_app
    - mls-app-01: x.x.x.x


    Done.

This can be useful if we want to execute a task only for a given node::

    $ fab frontend.restart_nginx:hosts=x.x.x.x
    [x.x.x.x] Executing task 'frontend.restart_nginx'
    [x.x.x.x] sudo: /etc/init.d/nginx restart
    [x.x.x.x] out: sudo password:
    [x.x.x.x] out: Restarting nginx: nginx.
    [x.x.x.x] out:


    Done.
    Disconnecting from x.x.x.x... done.


.. _`Propertyshelf`: http://propertyshelf.com
.. _`knife`: http://docs.opscode.com/knife.html
