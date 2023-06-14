#!/usr/bin/bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
. $SCRIPTPATH/vars.sh

/usr/bin/bash $SCRIPTPATH/format-code.sh
/usr/bin/bash $SCRIPTPATH/lint-code.sh
