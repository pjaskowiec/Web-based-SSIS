#!/bin/bash

source .venv/bin/activate
build_command=$(python fetch_db_creds.py --image-name student-crud --tag latest --build True)
run_command=$(python fetch_db_creds.py --image-name student-crud --tag latest)
pushd ../
   #$build_command
   echo $run_command
popd
