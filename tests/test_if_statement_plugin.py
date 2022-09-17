import subprocess
from textwrap import dedent


def test_actual_code(tmpdir):
    file = tmpdir / 'code.py'
    with file.open('w') as f:
        f.write(
            dedent(
                """
            x = 10
            if x == 1:
                y = 2
            else:
                y = 3
            if x == 1:
                z = 5
            if x == 10:
                print(10)  # noqa: T001
            else:
                print(5)  # noqa: T001
        """
            )
        )
    output = (
        subprocess.run(
            ['poetry', 'run', 'flake8', str(file)], stdout=subprocess.PIPE
        )
        .stdout.decode()
        .strip()
    )
    expected = (
        f'{tmpdir}/code.py:3:1: '
        f'IFS001 Use one liner if statement so as not to repeat the assignment to y'
    )
    assert output[: len(expected)] == expected
