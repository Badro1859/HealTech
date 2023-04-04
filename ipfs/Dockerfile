FROM ipfs/kubo:latest

ENV IPFS_PATH /data/ipfs
ENV IPFS_PROFILE server

# Enforce private network settings
ENV LIBP2P_FORCE_PNET 1
COPY swarm.key $IPFS_PATH
COPY init-config.sh /container-init.d/001-init.sh

EXPOSE 5001
EXPOSE 4001