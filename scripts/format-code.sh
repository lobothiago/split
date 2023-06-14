#!/usr/bin/bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
. $SCRIPTPATH/vars.sh

. $VENV/bin/activate && black -q $SRCS && isort $SRCS
