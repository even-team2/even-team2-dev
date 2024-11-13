#!/bin/bash

# stop running server
ps x | grep uvicorn | grep -v grep | awk '{print $1}' | xargs kill -9

# start server
. ./venv/bin/activate
nohup uvicorn main:app --host=0.0.0.0 > ./output.log 2>&1 &
