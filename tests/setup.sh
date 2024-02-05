function connect {
  swarm up -d --scale-bootstrap=4 >/dev/null 2>&1
  while [ "$(agent connect --container swarm-agent-user-1)" != "READY" ]; do sleep 1; done
  agent login local
}

function teardown {
  CONTAINERS=$(docker container ls -q)
  if test ! -z "${CONTAINERS}"; then
    docker container stop -t 1 ${CONTAINERS} >/dev/null 2>/dev/null
  fi
  rm -rf data/*/.hive/
}
export GID=$(id -g)
export UID
PATH=$PATH:${SRCDIR}
cd ${SRCDIR}
rm  config.json >/dev/null 2>&1
