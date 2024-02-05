# Quick Tutorial

## Build

Build the master branch:
```bash
./swarm.py build
```

Build a branch in your private fork:

```bash
./swarm.py build --agent-repo=hivenet-mathieu-lacage/hive-agent --agent-branch=master
```

## Start 

```bash
./swarm.py up -d
```

Alternatively, you can scale the topology:
```bash
./swarm.py up -d --scale-bootstrap=2
```

## Stop

```bash
docker compose down
```

## Inspect

Check the status of each service:
```bash
./swarm.py health
```

Look at the logs for agents:
```bash
tail -f data/swarm-agent-bootstrap-1/.hive/logs/agent.log
```

Get a shell in the agent environments:
```bash
./swarm.py shell bootstrap-1
```

## Debug

```bash
./swarm.py debug bootstrap-1
```

# How it works

1. During the build, we use a dockerfile that embeds the dlv debugger and we
   leave around all source files after the build
2. When you start the deployment, we generate automatically a couple of configuration
   files for each service and then we start dlv inside each container to start the agent
3. Finally, at runtime, when you want to connect to the debugger, you exec dlv inside
   the target container to connect to the dlv already running inside the container. This
   makes it easy for dlv to access the source code and symbols of the running agent.

