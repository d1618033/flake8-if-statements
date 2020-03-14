from textwrap import dedent

from flake8_plugin_utils import assert_error, assert_not_error

from flake8_if_statements.errors import AssignmentToSameVariable
from flake8_if_statements.visitor import IfStatementsVisitor


def test_if_statement_same_variable_assignment():
    code = dedent(
        """
        if x == 1:
            y = 2
        else:
            y = 5
    """
    )
    assert_error(
        IfStatementsVisitor, code, AssignmentToSameVariable, variables='y'
    )


def test_if_statement_same_variable_assignment_tuple_assignment():
    code = dedent(
        """
        if x == 1:
            y, z = 2, 3
        else:
            y, z = 4, 5
    """
    )
    assert_error(
        IfStatementsVisitor, code, AssignmentToSameVariable, variables='(y, z)'
    )


def test_if_statement_same_variable_assignment_tuple_within_tuple_assignment():
    code = dedent(
        """
        if x == 1:
            a = y, (z, w) = 2, (3, 9)
        else:
            a = y, (z, w) = 4, (5, 11)
    """
    )
    assert_error(
        IfStatementsVisitor,
        code,
        AssignmentToSameVariable,
        variables='a, (y, (z, w))',
    )


def test_if_statement_same_variable_assignment_list_assignment():
    code = dedent(
        """
        if x == 1:
            [y, [z, w]] = 2, (3, 9)
        else:
            [y, [z, w]] = 4, (5, 11)
    """
    )
    assert_error(
        IfStatementsVisitor,
        code,
        AssignmentToSameVariable,
        variables='[y, [z, w]]',
    )


def test_if_statement_same_variable_assignment_multiple_targets():
    code = dedent(
        """
        if x == 1:
            y = z = 2
        else:
            y = z = 4
    """
    )
    assert_error(
        IfStatementsVisitor, code, AssignmentToSameVariable, variables='y, z'
    )


def test_if_statement_same_variable_assignment_subscription():
    code = dedent(
        """
        if x == 1:
            y[0] = 2
        else:
            y[0] = 4
    """
    )
    assert_error(
        IfStatementsVisitor, code, AssignmentToSameVariable, variables='y[0]'
    )


def test_if_statement_same_variable_assignment_slice():
    code = dedent(
        """
        if x == 1:
            y[1:5:2] = 2
        else:
            y[1:5:2] = 4
    """
    )
    assert_error(
        IfStatementsVisitor,
        code,
        AssignmentToSameVariable,
        variables='y[1:5:2]',
    )


def test_if_statement_same_variable_assignment_attribute():
    code = dedent(
        """
        if x == 1:
            y.a.b = 2
        else:
            y.a.b = 4
    """
    )
    assert_error(
        IfStatementsVisitor, code, AssignmentToSameVariable, variables='y.a.b'
    )


def test_if_statment_different_variable_assignment():
    code = dedent(
        """
        if x == 1:
            y = 2
        else:
            z = 5
    """
    )
    assert_not_error(IfStatementsVisitor, code)


def test_if_statment_no_else():
    code = dedent(
        """
        if x == 1:
            y = 2
    """
    )
    assert_not_error(IfStatementsVisitor, code)


def test_if_statment_multiple_lines():
    code = dedent(
        """
        if x == 1:
            y = x + 1
            z = 5
        else:
            z = 6
    """
    )
    assert_not_error(IfStatementsVisitor, code)


def test_if_statment_non_assignment():
    code = dedent(
        """
        if x == 1:
            print(x)
        else:
            print(x+1)
    """
    )
    assert_not_error(IfStatementsVisitor, code)


def test_if_statment_inline():
    code = dedent(
        """
        y = 2 if x == 1 else 5
    """
    )
    assert_not_error(IfStatementsVisitor, code)
