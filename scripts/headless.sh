#!/usr/bin/env bash

locust --headless --users 10 --spawn-rate 1 -H http://your-server.com

