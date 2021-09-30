import unittest
from scrap_table import parse_table 
from helpers import TestingWithFixture, TestCaseFixtures, TestCaseWithFixture

class TestSeverityTables(TestingWithFixture):
    def test_parse(self) -> None:
        testcases: TestCaseFixtures = [
            TestCaseWithFixture(
                fixture_file='security_release_13-11-2_13-10-4_13-9-7.html',
                expected=[
                    {'key': 'Update Python dependency', 'value': 'Dependency Update - critical'},
                    {'key': 'Read API scoped tokens can execute mutations', 'value': 'high'},
                    {'key': 'Update Redis dependency', 'value': 'Dependency Update - high'},
                    {'key': 'Update carrierwave gem', 'value': 'Dependency Update - high'},
                    {'key': 'Update Mermaid npm package', 'value': 'Dependency Update - high'},
                    {'key': 'Pull mirror credentials are exposed', 'value': 'medium'},
                    {'key': 'Denial of Service when querying repository branches API',
                    'value': 'medium'},
                    {'key': 'Non-owners can set system_note_timestamp when creating / updating issues',
                    'value': 'medium'},
                    {'key': 'DeployToken will impersonate a User with the same ID when using Dependency Proxy','value': 'low'}
                ]
            ),
            TestCaseWithFixture(
                fixture_file='security_release_14-0-4.html',
                expected=[
                    {'value': 'critical', 'key': 'Arbitrary file read via design feature'},
                ]
            )
        ]

        self.with_fixtures(parse_table, testcases)

if __name__ == '__main__':
    unittest.main()
