#!/usr/bin/env bash
if gcloud pubsub topics describe okta-sync &> /dev/null; then
    echo "Topic okta-sync already exists." >&2
else
    gcloud pubsub topics create okta-sync
fi