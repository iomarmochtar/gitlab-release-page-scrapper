'''
scrap list of changes in patch release
'''
from typing import List
from bs4 import BeautifulSoup, element
from shared import get_req, target_url_from_arg, join_resultset

def parse_changes(html_content: str) -> List[str]:
    '''
    parse list of changes in list after first title
    '''
    parser = BeautifulSoup(html_content, 'html.parser')
    titles = parser.select('.content > h2')
    if not titles:
        return []

    first_title = titles[0]
    list_tag: element.Tag = first_title.find_next('ul')
    if not list_tag:
        return []

    a_list = list_tag.select('li > a')
    return join_resultset(a_list)

def main() -> None:
    '''
    main fn
    '''
    url = target_url_from_arg(
        'release patch',
        'https://about.gitlab.com/releases/2021/09/02/gitlab-13-12-11-released/'
    )

    html_content = get_req(url)
    print('\n'.join([ f'- {x}' for x in  parse_changes(html_content) ]))

if __name__ == '__main__':
    main()
