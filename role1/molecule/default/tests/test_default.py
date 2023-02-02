def test_example_role(host):  # pylint: disable=missing-module-docstring, missing-function-docstring
    role = host.ansible("include_role", "name=role1")
    assert role.rc == 0
    assert role.stderr == ""
