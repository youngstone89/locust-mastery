#!/usr/bin/env bash

locust --headless --users 10 --spawn-rate 1 -H http://localhost:3001/api/v1/minio/events

