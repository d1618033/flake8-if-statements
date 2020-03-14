from flake8_plugin_utils import Plugin

from flake8_if_statements.visitor import IfStatementsVisitor


class IfStatementsPlugin(Plugin):
    name = 'IfStatementsPlugin'
    version = '0.0.0'
    visitors = [IfStatementsVisitor]
