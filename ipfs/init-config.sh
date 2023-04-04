#!/bin/sh
set -ex
ipfs bootstrap rm all
ipfs config Routing.Type dht