FROM debian as build

RUN apt-get update && apt-get install -y \
	ca-certificates \
	openssh-client \
	git \
	wget

# install go
ENV GO_VERSION=go1.20.13.linux-arm64.tar.gz
RUN wget https://go.dev/dl/${GO_VERSION}
RUN tar -C /usr/local -xzf ${GO_VERSION}

ENV PATH=${PATH}:/usr/local/go/bin
ENV GOPATH=/usr/local/go


# The following tools make debugging oh so much easier
RUN apt-get update && apt-get install -y \
	dbus \
	net-tools \
	dnsutils \
	iproute2 \
	iputils-ping \
	traceroute \
	curl \
	netcat-openbsd \
	nmap \
	jq \
	python3 \
	python-is-python3 \
	vim 


# install dlv for debugging
#RUN go install github.com/go-delve/delve/cmd/dlv@latest

ARG AGENT_GIT_REPO
ARG AGENT_GIT_BRANCH
ARG AGENT_BUILD_TAG

# Make sure we have a key for github.com
RUN mkdir -p ~/.ssh/
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

# clone hive-agent
ARG AGENT_GIT_VERSION=unknown
WORKDIR /source
RUN --mount=type=ssh git clone git@github.com:$AGENT_GIT_REPO.git hive-agent --recurse-submodules
WORKDIR /source/hive-agent
RUN git checkout $AGENT_GIT_BRANCH

# Build hive-agent
RUN go mod tidy
COPY const_custom.go env/
RUN GOOS=linux GOARCH=arm64 CGO_ENABLED=0 go build -gcflags="all=-N -l" -a -tags custom -o /hive-agent main.go
