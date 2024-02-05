#!/bin/bash

container_name() {
	IP=`ifconfig eth0 | grep 'inet ' | awk '{print $2}'`
	SERVICE=`dig -x $IP +short | cut -d'.' -f1`
	echo ${SERVICE}
}
HOME=/data/$(container_name)
cd $HOME
/hive-agent --token $1
