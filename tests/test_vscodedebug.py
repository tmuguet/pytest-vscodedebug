# -*- coding: utf-8 -*-


def test_help_message(testdir):
    result = testdir.runpytest(
        "--help",
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*vscodedebug:",
            "*--vscodedebug*Enables debugging",
            "*--vscodedebug-port=*",
        ],
    )
