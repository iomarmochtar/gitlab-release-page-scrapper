import unittest
from os.path import join
from typing import List, Any, Callable, NewType, Type

class TestCaseWithFixture:
    fixture_file: str = ''
    expected: List[Any] = []

    def __init__(self, fixture_file: str, expected: List[Any]) -> None:
        self.fixture_file = fixture_file
        self.expected = expected

TestCaseFixtures = NewType("TestCaseFixtures", List[Type[TestCaseWithFixture]])

class TestingWithFixture(unittest.TestCase):
    def with_fixtures(self, fn_to_test: Callable,  testcases: TestCaseFixtures) -> None:
        for tc in testcases:
            with open(join('tests', 'fixtures', tc.fixture_file), 'r') as fp:
                actual = fn_to_test(fp.read())
                self.assertListEqual(
                    tc.expected,
                    actual,
                )
