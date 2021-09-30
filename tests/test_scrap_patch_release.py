import unittest
from scrap_patch_release import parse_changes
from helpers import TestingWithFixture, TestCaseFixtures, TestCaseWithFixture

class TestScrapPatchRelease(TestingWithFixture):
    def test_parse_changes(self) -> None:
        testcases: TestCaseFixtures = [
            TestCaseWithFixture(
                    fixture_file='patch_release_13_12_11.html', 
                    expected=[
                        'Only activate Git pack-objects hook if cache is enabled',
                        'Backport improved replication logic'
                    ]
                ),
            TestCaseWithFixture(
                    fixture_file='patch_release_14-0-8.html', 
                    expected=[
                        'Revert backfill on ci_build_trace_sections',
                        'Resolve "operator does not exist: integer[] || bigint in app/models/namespace/traversal_hierarchy.rb"',
                        'Fix Sidekiq workers delete each other\'s metrics',
                        'Geo 2.0 Regression - Add ability to remove primary',
                        'Backport fix for flaky spec to 14.0'
                    ]
                )
        ] 

        self.with_fixtures(parse_changes, testcases)

if __name__ == '__main__':
    unittest.main()
