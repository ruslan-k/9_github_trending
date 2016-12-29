from datetime import date, timedelta

import requests


def get_trending_repositories(top_size):
    week_ago = date.today() - timedelta(days=7)
    repo_search__url = 'https://api.github.com/search/repositories'
    search_data = {
        'q': 'created:>={}'.format(week_ago),
        'sort': 'stars',
        'per_page': top_size,
    }
    response = requests.get(repo_search__url, params=search_data)
    repos_data = response.json()['items']
    return repos_data


def get_open_issues_amount(repositories):
    for num, repository in enumerate(repositories):
        print("""{num} {name}\nURL: {url}\nOpen Issues: {issues}\n""".format(
            num=num + 1,
            name=repository['full_name'],
            url=repository['clone_url'],
            issues=repository['open_issues'],
        ))

if __name__ == '__main__':
    trending_repositories = get_trending_repositories(20)
    get_open_issues_amount(trending_repositories)
