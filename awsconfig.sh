#!/bin/sh

aws configure set aws_access_key_id "${x}" && aws configure set aws_secret_access_key "${y}" && aws configure set region "${z}" && aws configure set output "none"

exec python3 app.py