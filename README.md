# Okta IP Range Sync
This function updates Google Cloud Platform firewall rules to allow egress to IP ranges from Okta's [published IP ranges](https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json). This enables compute instances to access Okta's servers.

## Prepare
1. Create egress firewall rules in GCP using the format `okta-[okta-cell]`. You can find the Okta cell names in the [published IP ranges](https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json); replace underscores (`_`) with dashes (`-`).
2. Run `make prepare` to create a PubSub topic that you can use with Cloud Scheduler to invoke the function on a schedule.

## Deployment
To deploy, use `make deploy`.

## Usage
Invoke the function using the Cloud Functions console page or using Cloud Scheduler with PubSub.
