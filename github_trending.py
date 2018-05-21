from datetime import (
    datetime,
    timedelta
)
import requests


def get_open_issues_for_repo(repo_url):
    issues_url = '/'.join([repo_url, 'issues'])
    issues_data = requests.get(
        issues_url,
        params={'state': 'open'}
    )
    try:
        return True, issues_data.json()
    except ValueError:
        return False, None


def load_repositories_from_github(page_number, date_begin):
    query_params = {
        'q': 'created:>{}'.format(date_begin),
        'sort': 'stars',
        'page': page_number
    }

    response = requests.get(
        'https://api.github.com/search/repositories',
        params=query_params
    )

    try:
        return True, response.json()
    except ValueError:
        return False, None


def get_trending_repositories(repository_limit_to_process, date_begin):
    repositories_remains_to_process = repository_limit_to_process
    current_page_number = 1

    while repositories_remains_to_process:
        has_data, repositories_data = load_repositories_from_github(
            current_page_number,
            date_begin
        )

        if not has_data:
            break

        to_process = min(repositories_remains_to_process, len(repositories_data['items']))

        for current_repository in repositories_data['items'][:to_process]:
            yield current_repository

        repositories_remains_to_process -= to_process


if __name__ == '__main__':

    repository_limit_to_process = 20
    days_before_limit = 7
    date_begin = (datetime.now() - timedelta(days=days_before_limit)).strftime('%Y-%m-%d')

    last_week_github_repositories = get_trending_repositories(
        repository_limit_to_process,
        date_begin
    )

    for repository in last_week_github_repositories:

        has_issues, issues_for_repo = get_open_issues_for_repo(
            repository['url'],
        )

        print('Repo: {}, stargazers count: {}'.format(
            repository['url'],
            repository['stargazers_count'])
        )

        if has_issues and isinstance(issues_for_repo, list):
            print('Issues count: {}'.format(len(issues_for_repo)))
            for current_issues in issues_for_repo:
                print('\tIssue url: {}'.format(current_issues['url']))
