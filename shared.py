'''
collection of shared functions
'''
from urllib.request import Request, urlopen
from argparse import ArgumentParser
from typing import List
from bs4 import element

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'

def get_req(url: str) -> str:
    '''
    fetch html content (GET method)
    '''
    request = Request(url)
    request.add_header('User-Agent', USER_AGENT)

    return urlopen(request).read()

def target_url_from_arg(func: str, sample_url: str) -> str:
    '''
    common arguments
    '''
    parser = ArgumentParser(description=f'Gitlab release scrapper for {func}')
    parser.add_argument('-u', '--url',
        help=f'URL of gitlab release page, eg: {sample_url}', required=True)
    args = parser.parse_args()
    return args.url

def join_tag_contents(tag: element.Tag) -> str:
    '''
    get contents of tag
    '''
    return ''.join([x.string for x in tag.contents])

def join_resultset(result_set: element.ResultSet) -> List[str]:
    '''
    an helper for iterrate the cleaned content tag from a result set
    '''
    return [join_tag_contents(tag) for tag in result_set]
