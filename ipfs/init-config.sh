#!/bin/sh
set -ex
ipfs bootstrap rm all
ipfs config Routing.Type dht
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "POST", "GET"]'