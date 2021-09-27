'''
scrap release page for feature points
'''
from typing import List, NewType, Dict, cast
from bs4 import BeautifulSoup, element
from shared import get_req, target_url_from_arg

FeatureList = NewType('FeatureList', List[str])

def join_tag_contents(tag: element.Tag) -> str:
    '''
    get contents of tag
    '''
    return ''.join([x.string for x in tag.contents])

def join_resultset(result_set: element.ResultSet) -> FeatureList:
    '''
    an helper for iterrate the cleaned content tag from a result set
    '''
    return cast(FeatureList, [join_tag_contents(tag) for tag in result_set])

class ParseFeatures:
    '''
    parse release page for it's feature components
    '''
    _bs: BeautifulSoup

    def __init__(self, html_content: str) -> None:
        self._bs = BeautifulSoup(html_content, 'html.parser')

    def _list_by_sibling_id(self, tag_id: str, title_tag: str = 'h3') -> FeatureList:
        '''
        get list of anchor tag using by it's sibling title id
        '''
        title = self._bs.find(title_tag, {'id': tag_id})
        a_list = title.find_next('ul').select('li > a')
        return cast(FeatureList, [join_tag_contents(x) for x in a_list])

    def parse_bug_fixes(self) -> FeatureList:
        '''
        parse list of bug fix
        '''
        return self._list_by_sibling_id('bug-fixes')

    def parse_performances(self) -> FeatureList:
        '''
        parse list performance improvements
        '''
        return self._list_by_sibling_id('performance-improvements')

    def parse_ui_improvements(self) -> FeatureList:
        '''
        parse list of ui improvements
        '''
        return self._list_by_sibling_id('usability-improvements')

    def parse_key_improvements(self) -> FeatureList:
        '''
        parse list of key/highlighted features or improvements
        '''
        return join_resultset(self._bs.select('div.column > h2 > p'))

    def parse_improvements(self) -> FeatureList:
        '''
        parse list of non major improvements
        '''
        return join_resultset(self._bs.select('div.secondary-column-feature > h3 > p'))

    def parse_deprecations(self) -> FeatureList:
        '''
        parse list of deprecations
        '''
        return join_resultset(self._bs.select('section#deprecations > h3 > p'))

    def parse_removals(self) -> FeatureList:
        '''
        parse list of removals
        '''
        return join_resultset(self._bs.select('section#removals > h3 > p'))

    @property
    def results(self) -> Dict[str, FeatureList]:
        '''
        get list of parsed item list
        '''
        return {
            'key_improvements': self.parse_key_improvements(),
            'improvements': self.parse_improvements(),
            'performances': self.parse_performances(),
            'bug_fixes': self.parse_bug_fixes(),
            'ui_improvements': self.parse_ui_improvements(),
            'deprecations': self.parse_deprecations(),
            'removals': self.parse_removals()
        }

def main() -> None:
    '''
    main func
    '''
    url = target_url_from_arg(
        'feature list',
        'https://about.gitlab.com/releases/2021/09/22/gitlab-14-3-released/'
    )

    html_content = get_req(url)
    parser = ParseFeatures(html_content)
    for k, flist in parser.results.items():
        title = k.replace('_', ' ').capitalize()
        print(title)
        print('=' * len(title))
        for feature in flist:
            print(f'- {feature}')
        print('\n')

if __name__ == '__main__':
    main()
