from datetime import datetime, timedelta
import requests


def get_open_issues_for_repo(repo_url):
    issues_url = '/'.join([repo_url, 'issues'])
    issues_data = requests.get(
        issues_url,
        params={'state': 'open'}
    )
    try:
        return issues_data.json()
    except ValueError:
        return None


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
        return response.json()
    except ValueError:
        return None


def get_trending_repositories(repository_to_process_limit, date_begin):
    repositories_qty_remains_to_process = repository_to_process_limit
    current_page_number = 1

    while repositories_qty_remains_to_process:
        repositories_data = load_repositories_from_github(
            current_page_number,
            date_begin
        )

        if repositories_data is None:
            break

        if not ('items' in repositories_data and isinstance(repositories_data['items'], list)):
            break

        to_process_qty = min(repositories_qty_remains_to_process, len(repositories_data['items']))

        for current_repository in repositories_data['items'][:to_process_qty]:
            yield current_repository

        repositories_qty_remains_to_process -= to_process_qty
        current_page_number += 1


if __name__ == '__main__':

    repository_to_process_limit = 20
    search_period_limit = 7
    date_begin = (datetime.now() - timedelta(days=search_period_limit)).strftime('%Y-%m-%d')

    github_repositories = get_trending_repositories(
        repository_to_process_limit,
        date_begin
    )

    for repository in github_repositories:

        issues_for_repo = get_open_issues_for_repo(
            repository['url'],
        )

        print('Repo: {}, stargazers count: {}'.format(
            repository['url'],
            repository['stargazers_count'])
        )

        if issues_for_repo is not None and isinstance(issues_for_repo, list):
            print('Issues count: {}'.format(len(issues_for_repo)))
            for current_issues in issues_for_repo:
                print('\tIssue url: {}'.format(current_issues['url']))
