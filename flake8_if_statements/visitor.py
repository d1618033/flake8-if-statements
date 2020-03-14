import ast
from typing import Any, List, Optional

import astor
from flake8_plugin_utils import Visitor

from flake8_if_statements.errors import AssignmentToSameVariable


class IfStatementsVisitor(Visitor):
    def _get_targets(self, body: List[Any]) -> Optional[List[str]]:
        if len(body) != 1:
            return None
        assignment = body[0]
        if not isinstance(assignment, ast.Assign):
            return None
        return [
            astor.code_gen.to_source(target).strip()
            for target in assignment.targets
        ]

    def visit_If(self, node: ast.If) -> None:  # noqa: N802
        body_targets = self._get_targets(node.body)
        if body_targets is None:
            return
        orelse_targets = self._get_targets(node.orelse)
        if body_targets == orelse_targets:
            self.error_from_node(
                AssignmentToSameVariable,
                node,
                variables=', '.join(body_targets),
            )
