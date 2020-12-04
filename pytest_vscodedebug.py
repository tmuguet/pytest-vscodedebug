# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup("vscodedebug")
    group.addoption(
        "--vscodedebug",
        action="store_true",
        default=False,
        dest="vscodedebug",
        help="Enables debugging",
    )
    group.addoption(
        "--vscodedebug-port",
        action="store",
        type=int,
        default=10001,
        dest="vscodedebug_port",
        help="Port for debugger to listen on",
    )


def pytest_collection_finish(session: pytest.Session) -> None:
    # From https://blog.theodo.com/2020/05/debug-flask-vscode/
    if session.config.option.vscodedebug:
        import multiprocessing

        process = multiprocessing.current_process()
        if process.pid and process.pid > 1:
            import debugpy

            debugpy.listen(("0.0.0.0", session.config.option.vscodedebug_port))
            print(
                "⏳ VS Code debugger can now be attached on port {}".format(
                    session.config.option.vscodedebug_port
                ),
                flush=True,
            )
            debugpy.wait_for_client()
            print("⚙️ VS Code debugger attached", flush=True)
