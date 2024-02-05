  $ . ${TESTDIR}/setup.sh
  $ teardown
  $ connect
  $ agent workspace create 12345 >/dev/null 2>&1
  $ agent fs pwd
  /
  $ agent fs ls
  volume  default
  $ agent fs ls /
  volume  default
  $ agent fs cd default
  $ agent fs ls
  $ agent fs ls /
  volume  default
  $ agent fs mkdir a
  $ agent fs ls
  directory  a
  $ agent fs ls /default
  directory  a
  $ agent fs mkdir -p /default/b/c/d
  $ agent fs ls
  directory  a
  directory  b
