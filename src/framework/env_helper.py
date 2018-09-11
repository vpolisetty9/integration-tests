import json
import os
from src.framework.env_config import env_config

class EnvHelper:
    env = json.loads(env_config)
    test_env = os.environ.get("TEST_ENV") if os.environ.get("TEST_ENV") is not None else "STG"
    test_target = os.environ.get("TEST_TARGET") if os.environ.get("TEST_TARGET") is not None else "desktop_chrome"

    @staticmethod
    def get_test_env():
        return EnvHelper.test_env

    @staticmethod
    def get_test_target():
        return EnvHelper.test_target

    @staticmethod
    def get_app_url():
        return EnvHelper.env[EnvHelper.get_test_env()]["URL"]

    # returns 'desktop' or 'mobile'
    @staticmethod
    def get_test_target_context():
        return EnvHelper.get_test_target().split('_')[0]