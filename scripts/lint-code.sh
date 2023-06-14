#!/usr/bin/bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
. $SCRIPTPATH/vars.sh

# Formatting
. $VENV/bin/activate && black --check --diff -q $SRCS

# Imports
. $VENV/bin/activate && isort --check $SRCS

# MyPy
. $VENV/bin/activate && mkdir -p .mypy-cache && mypy --non-interactive --install-types --ignore-missing-imports $SRCS

# ## Lint Python code - formatting check
# lint-python-format-check:
# 	. $(MAIN_VENV)/bin/activate \
# 	  && black --check --diff -q $(PYTHON_SRCS)

# ## Lint Python code - imports check
# lint-python-imports-check:
# 	. $(MAIN_VENV)/bin/activate \
# 	  && isort --check $(PYTHON_SRCS)

# ## Lint Python code - mypy check
# lint-python-mypy-check:
# 	. $(MAIN_VENV)/bin/activate \
# 	  && mkdir -p .mypy_cache \
# 	  && mypy \
# 	    --non-interactive \
# 		--install-types \
# 		--ignore-missing-imports $(PYTHON_SRCS)