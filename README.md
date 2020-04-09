# Okta IP Range Sync
This function updates firewall rules to allow egress to IP ranges from Okta's [published IP ranges](https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json). This enables compute instances to access Okta's servers.

## Prepare
Ensure that there are firewall rules already created in the form of: `okta-[okta-cell]`. Replace the underscores `_` in Okta cells with `-`.

## Usage
To deploy, use `make deploy`.

