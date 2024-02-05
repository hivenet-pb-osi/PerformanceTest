#!/bin/bash

if test ! -d ${HOME}/.hive; then
	mkdir -p ${HOME}/.hive
fi
if test ! -f ${HOME}/.hive/config.yaml; then
	/hive-agent -c ${CLASS} config init
fi

