#!/usr/bin/env bash

REDIS_HOST=localhost
REDIS_PORT=6379

IFS=$'\n'
echo "<<<redis_cluster_state:sep(59)>>>"
for host in `echo 'CLUSTER NODES' | nc ${REDIS_HOST} ${REDIS_PORT} | tr -d $'\x0d' | tail -n+2`; do
  NODE_ID=`echo "${host}" | cut -d' ' -f1`
  NODE_ADDRESS=`echo "${host}" | cut -d' ' -f2`
  NODE_FLAGS=`echo "${host}" | cut -d' ' -f3`
  NODE_MASTER_ID=`echo "${host}" | cut -d' ' -f4`
  NODE_PENDING_PING_TIMESTAMP=`echo "${host}" | cut -d' ' -f5`
  NODE_LAST_PING_RESPONSE=`echo "${host}" | cut -d' ' -f6`
  NODE_CONFIG_EPOCH=`echo "${host}" | cut -d' ' -f7`
  NODE_LINK_STATE=`echo "${host}" | cut -d' ' -f8`
  NODE_SLOTS=`echo "${host}" | cut -d' ' -f9`

  NODE_HOST=`echo "${NODE_ADDRESS}" | cut -d':' -f1`
  NODE_PORT=`echo "${NODE_ADDRESS}" | cut -d':' -f2`

  for e in `echo 'CLUSTER INFO' | nc ${NODE_HOST} ${NODE_PORT} | tr -d $'\x0d' | tail -n+2 | fgrep 'cluster_'`; do
    name=`echo -n "${e}" | cut -d':' -f1`
    val=`echo -n "${e}" | cut -d':' -f2`
    export ${name^^}=${val}
  done

  echo "${NODE_ID};${NODE_ADDRESS};${NODE_FLAGS};${CLUSTER_STATE};${CLUSTER_SIZE};${CLUSTER_KNOWN_NODES};${CLUSTER_SLOTS_FAIL};${CLUSTER_SLOTS_PFAIL}"
done
