import logging
import os

import pytest

from splitr.lib.service.config_service import ConfigService


@pytest.fixture
def create_env_vars(request):
    log = logging.getLogger(__name__)
    log.info("Running create_env_vars")

    if hasattr(request, "param"):
        for key, value in request.param.items():
            os.environ[key] = str(value)


@pytest.fixture
def config_service(create_env_vars):
    return ConfigService()


@pytest.mark.parametrize(
    "create_env_vars", [{"test": 123}], indirect=["create_env_vars"]
)
def test_load_env_var(config_service: ConfigService):

    log = logging.getLogger(__name__)

    log.info(f"inside test {os.environ.get('test')}")

    # TODO: handle upper vs lower case in config service impl
