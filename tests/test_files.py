import sys
from io import StringIO
from unittest.mock import patch


def test_stdout():
    test_args = ["moban", "-t", "{{'tests' is directory}}"]
    with patch.object(sys, "argv", test_args):
        with patch("sys.stdout", new_callable=StringIO) as fake_stdout:
            from moban.main import main

            main()
            assert fake_stdout.getvalue() == "True\n"
