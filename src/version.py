from configparser import ConfigParser

cf = ConfigParser()

cf.read('pyproject.toml')


def get_service_version():
    return cf['tool.poetry']['version'].strip('"')


def get_project_name():
    return cf['tool.poetry']['name'].title()


def main():
    print(f"{cf['tool.poetry']['name'].title()} running at version: {cf['tool.poetry']['version']}")
