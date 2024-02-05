  $ . ${TESTDIR}/setup.sh
  $ teardown
  $ connect
  $ agent workspace read
  No workspace
  $ agent workspace create 12345 | jq -r .read_key
  [a-f0-9]+ (re)
  $ agent workspace create 12345 | jq .code
  409
  $ WORKSPACE_MID=$(agent workspace read | jq -r .workspace_mid)
  $ echo ${WORKSPACE_MID}
  [a-f0-9]+ (re)
  $ agent workspace read ${WORKSPACE_MID} | jq -r .workspace_mid
  [a-f0-9]+ (re)
