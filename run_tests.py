#!/usr/bin/env python

import unittest
import os
import sys
import fnmatch


def get_test_dirs(path):
    """get_test_dirs(path) => list

    Returns a list of direcotries and subdirectories with Pyton tests.
    """

    test_dirs = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if fnmatch.fnmatch(filename, 'test_*.py'):
                test_dirs.append(root)
                break
    return test_dirs

def run_tests_in(test_dirs=['.']):
    """run_tests_in(path) => True or False

    Run all the tests until they end or one fails. It returns True if
    all the tests pass and False if any of them fails.
    """
    for test_dir in test_dirs:
        sys.stderr.write("Testing: %s\n" % test_dir)
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(test_dir)
        test_runner = unittest.TextTestRunner(verbosity=2)
        result = test_runner.run(test_suite)
        if not result.wasSuccessful():
            return False
    return True


if __name__ == '__main__':
    # It can take one directory as argument, but only one.
    # If zero,more than one agrument are passed or the argument isn't a valid
    # directory, it will use the script's directory.
    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        root_dir = sys.argv[1]
    else:
        root_dir = os.path.dirname(__file__)

    test_dirs = get_test_dirs(root_dir)
    was_successful = run_tests_in(test_dirs)
    if not was_successful:
        sys.exit(1)
