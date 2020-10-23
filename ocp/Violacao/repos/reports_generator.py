from ocp.Violacao.repos.reports.html_generator import HTMLGenerator
from ocp.Violacao.repos.reports.markdown_generator import MarkdownGenerator


class ReportsGenerator():
    @classmethod
    def build(cls, type, repos):
        if type == 'HTML':
            return HTMLGenerator.build(repos)
        elif type == 'MARKDOWN':
            return MarkdownGenerator.build(repos)
        else:
            return "Invalid report type!"