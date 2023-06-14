import json
import logging
import os
from typing import Any, Dict, Optional


class ConfigService(dict):
    def __init__(self) -> None:
        self._log = logging.getLogger(__name__)

        spec = {"test": "int"}

        for key, value in self._load_env_vars(spec).items():
            self.__setitem__(key, value)
            self.__setattr__(key, value)

    def _load_env_var_as_str(self, name: str) -> Optional[str]:
        result = os.environ.get(name, None)

        return result

    def _load_env_var_as_int(self, name: str) -> Optional[int]:
        loaded_as_str = self._load_env_var_as_str(name)
        result = None

        if loaded_as_str:
            try:
                result = int(loaded_as_str)
            except Exception as e:
                self._log.error(
                    f"Couldn't load env var `{name}` with str value `{loaded_as_str}` as int"
                )
                raise e

        return result

    def _load_env_var_as_bool(self, name: str) -> Optional[bool]:
        loaded_as_str = self._load_env_var_as_str(name)
        result = None

        if loaded_as_str:
            try:
                result = bool(loaded_as_str)
            except Exception as e:
                self._log.error(
                    f"Couldn't load env var `{name}` with str value `{loaded_as_str}` as bool"
                )
                raise e

        return result

    def _load_env_var_as_dict(self, name: str) -> Optional[Dict]:
        loaded_as_str = self._load_env_var_as_str(name)
        result = None

        if loaded_as_str:
            try:
                result = json.loads(loaded_as_str)
            except Exception as e:
                self._log.error(
                    f"Couldn't load env var `{name}` with str value `{loaded_as_str}` as dict"
                )
                raise e

        return result

    def _load_env_vars(self, spec: Dict[str, str], **kwargs) -> Dict[str, Any]:
        result = {}

        for variable_name, type in spec.items():
            type = type.lower()

            value: Any = None

            if type == "int":
                value = self._load_env_var_as_int(variable_name)
            elif type == "bool":
                value = self._load_env_var_as_bool(variable_name)
            elif type == "json" or type == "dict":
                value = self._load_env_var_as_dict(variable_name)
            else:
                value = self._load_env_var_as_str(variable_name)

            result[variable_name] = value

        result.update(**kwargs)

        return result
