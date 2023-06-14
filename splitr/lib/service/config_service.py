from typing import Optional
import os

class ConfigService(dict):

    def __init__(self) -> None:
        pass

    def _load_env_var_as_int(self) -> Optional[int]:
        pass

    def _load_env_var_as_bool(self) -> Optional[bool]:
        pass

    def _load_env_var_as_string(self, name : str) -> Optional[str]:
        return 

    def _load_env_vars(self):
        os.environ.get()

        pass