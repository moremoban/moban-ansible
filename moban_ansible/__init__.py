# flake8: noqa
from moban_ansible._version import __version__
from moban_ansible._version import __author__
from lml.loader import scan_plugins_regex

ANSIBLE_LIBRARIES = "^moban_ansible_.+$"
ANSIBLE_EXTENSIONS = [
    "moban_ansible.tests.files",
]


scan_plugins_regex(ANSIBLE_LIBRARIES, "moban", None, ANSIBLE_EXTENSIONS)
