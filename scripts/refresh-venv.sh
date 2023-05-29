#!/usr/bin/bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

/usr/bin/bash $SCRIPTPATH/pip-compile.sh
/usr/bin/bash $SCRIPTPATH/pip-install-requirements.sh
