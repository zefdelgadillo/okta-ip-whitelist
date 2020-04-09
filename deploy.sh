#!/usr/bin/env bash
gcloud functions deploy okta-ip-sync \
    --source=./src/ \
    --entry-point main \
    --runtime python37 \
    --trigger-topic okta-ip-sync \
    --env-vars-file .env.yaml
