#!/bin/bash

source .venv/bin/activate
build_command=$(python fetch_db_creds.py --image-name student-crud --tag latest)
pushd ../
   echo $build_command
popd