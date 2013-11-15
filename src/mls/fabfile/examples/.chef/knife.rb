# Logging.
log_level                         :info
log_location                      STDOUT

# Chef server configuration.
chef_server_url                   "#{ENV['PS_KNIFE_CHEF_SERVER']}"
client_key                        "#{ENV['PS_KNIFE_CLIENT_KEY']}"
node_name                         "#{ENV['PS_KNIFE_NODE_NAME']}"
validation_client_name            "#{ENV['PS_KNIFE_VALIDATION_CLIENT_NAME']}"
validation_key                    "#{ENV['PS_KNIFE_VALIDATION_CLIENT_KEY']}"
encrypted_data_bag_secret         "#{ENV['PS_ENCRYPTED_DATA_BAG_SECRET_FILE']}"

# Rackspace API configuration.
knife[:rackspace_api_key]       = "#{ENV['PS_RACKSPACE_API_KEY']}"
knife[:rackspace_api_username]  = "#{ENV['PS_RACKSPACE_USERNAME']}"
knife[:rackspace_endpoint]      = "#{ENV['PS_RACKSPACE_ENDPOINT']}"
knife[:rackspace_version]       = "#{ENV['PS_RACKSPACE_VERSION']}"
