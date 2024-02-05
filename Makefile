test:
	SRCDIR=$(shell pwd) cram -v ./tests

.PHONY: test
