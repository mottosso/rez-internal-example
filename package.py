name = "internal_example"
version = "1.1.0"

build_command = "python -m rezutils {root}"
private_build_requires = ["rezutils-1"]


def commands():
    global env
    env["PYTHONPATH"] = "{root}/python"
