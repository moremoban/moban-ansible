isort $(find moban_ansible -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 moban_ansible
black -l 79 tests
