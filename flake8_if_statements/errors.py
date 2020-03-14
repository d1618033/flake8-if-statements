from flake8_plugin_utils import Error


class AssignmentToSameVariable(Error):
    code = 'IFSTMT001'
    message = 'Use one liner if statement so as not to repeat the assignment to {variables}'
