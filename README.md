# hive-swarm

Create a local swarm of hive-agents based on docker / docker-compose

## User guide

Installing requirements

-   Go 1.19
-   Docker
-   Correctly set-up github tokens

SetUp Environment
export DOCKERHUB_USERNAME, DOCKERHUB_TOKEN, DOCKER_REPO dependent parameters as documented in the below confluence page
https://hiveteam.atlassian.net/wiki/spaces/EN/pages/144998440/Local+Docker+Swarm+Setup

Bootstrap the docker swarm for hive

```bash
./scripts/swarmtest.sh
```

Run the healthcheck of the hive swarm

```bash
docker exec -w /home/hive/ hive-swarm-ubee-1 /home/hive/healthcheck.sh
```

Run the smoketest

```bash
docker exec -w /home/hive/ hive-swarm-ubee-1 /home/hive/smoketest.sh
```

Run the performance test

```bash
docker exec -w /home/hive/ hive-swarm-ubee-1 /home/hive/perftests.sh
```

Destroy the local swarm ( run in the hive-swarm directory )

```bash
docker compose down
```

Connect to the container manually and run the smoke test script

```bash
docker exec -it hive-swarm-ubee-1 /bin/bash
cd /home/hive
./smoketest.sh
```
