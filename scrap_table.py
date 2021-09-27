'''
scrap list of security related release in table
'''
from functools import cmp_to_key
from typing import cast, Dict, List, NewType, Any
from bs4 import BeautifulSoup, element
from shared import get_req, target_url_from_arg

KV = NewType("KV", Dict[str, Any])

def parse_table(html_content: str) -> List[KV]:
    '''
    scrap table of vurn and ordering it by it's severity
    '''
    result: List[KV] = []
    parser = BeautifulSoup(html_content, 'html.parser')
    h2_title = parser.find(id='table-of-fixes')
    if not h2_title:
        return result

    tbl_tag: element.Tag = h2_title.findNext('table')
    if not tbl_tag:
        return result

    rows = tbl_tag.select('tbody > tr')
    for row in rows:
        title_col, severity = row.find_all('td')
        title_link: element.Tag = title_col.find('a')
        result.append(cast(KV, {
            'key': title_link.string,
            'value': severity.string
        }))

    def score_severity(sev: str) -> int:
        score = 4
        if 'critical' in sev:
            score = 0
        elif 'high' in sev:
            score = 1
        elif 'medium' in sev:
            score = 2
        elif 'low' in sev:
            score = 3
        return score

    def sort_by_sev(item1: KV, item2: KV) -> int:
        return score_severity(item1['value']) - score_severity(item2['value'])

    return cast(List[KV], sorted(result, key=cmp_to_key(sort_by_sev)))

def main() -> None:
    '''
    main fn
    '''
    url = target_url_from_arg(
        'list of vurnelbilities',
        'https://about.gitlab.com/releases/2021/04/28/security-release-gitlab-13-11-2-released/'
    )

    html_content = get_req(url)
    for parsed in parse_table(html_content):
        print(f"- {parsed['key']} [{parsed['value']}]")

if __name__ == '__main__':
    main()
