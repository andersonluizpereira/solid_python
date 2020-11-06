from dip.Solucao.repos.reports.writer import ReportWriter
from isp.Solucao.Models.manager import Manager
from isp.Solucao.Models.member import Member
from isp.Solucao.Models.user import User
from ocp.Solucao.repos.reports.html_generator import HTMLGenerator
from ocp.Solucao.repos.reports.markdown_generator import MarkdownGenerator
from ocp.Solucao.repos.reports_generator import ReportsGenerator
from srp.Solucao.github.client import GithubClient
from srp.Solucao.repo.parser import RepoParser

if __name__ == '__main__':
    username = 'andersonluizpereira'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)
        ReportWriter.write(markdown_report)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])

    member = Member('andersonluizpereira', 'andy2903.alp@gmail.com')
    user = User('andersonluizpereira', 'andy2903.alp@gmail.com')
    manager = Manager('andersonluizpereira', 'andy2903.alp@gmail.com')

    print(member.members())
    print(user)

    print(member.work())
    print(manager.work())
