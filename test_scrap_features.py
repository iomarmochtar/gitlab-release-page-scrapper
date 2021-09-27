from logging import NOTSET
import unittest
from os.path import join
from scrap_features import ParseFeatures
from scrap_table import parse_table 

class TestParseFeatures(unittest.TestCase):
    def setUp(self) -> None:
        with open(join('fixtures', 'major_release_14-0.html')) as fp:
            self.obj = ParseFeatures(fp.read())

    def test_parse_bug_fixes(self) -> None:
        expected = [
            'Cleanup policies can get stuck in the ongoing status',
            'Activity filter on Vulnerability Report throws error on group level dashboard',
            'Scanner filter on pipeline security tab does not filter results',
            'Misleading Dockerfile not found error in container-scanning',
            'Daily container scanning updates are broken',
            'cilium 1.8.1 chart not behaving well in recent versions of GKE',
            'Shared filtered search bar does not allow selecting multiple labels',
            'VSA - Unable to add new label filter after removing a label filter',
            'VSA - persisted default stage cannot be removed or edited',
            'DevOps Adoption tooltip shows incorrect data',
            'Productivity Analytics: Trendline chart not loading because n.response undefined',
            'Label filtering not working for Slack notifications integration',
            'diffs_metadata returning 500 error',
            'Unable to edit MR with unchecked mergeability state',
            'Cannot view old diff versions of merge request',
            '“Prevent MR approvals by the author” is ignored unless checked, saved, and unchecked',
            'SSH key expiration notification emails not sent for SSH keys expiring in the past',
            'Projects getting stuck indexing forever and using lots of resources',
            'Merge Request reference is wrong in Global Search result',
            '“Cancel Pipeline” button is visible to users without permission',
            'only external_pull_requests with changes is not working',
            'Using optional needs causes rendering error in pipeline view',
            'Use the correct Gitpod URL in User Preferences for self-managed instances',
            'Fix gitlab:incoming_email:check rake task after changes in 13.12',
            'Remove extra character from description field in Requirement export',
            'Prevent Service Desk emails from being rejected when you use a non-unique project suffix',
            'Fix some filters that do not work with GraphQL board lists',
            'GraphQL EpicsResolver does not handle timeframe arguments',
            'Notifications switch cannot be enabled for projects where it previously could be',
            'Mermaid stateDiagram-v2 with state description is not rendered',
            'Delay in updating open merge request and issue count badges on Geo secondary'
            ] 
        self.assertListEqual(self.obj.parse_bug_fixes(), expected)

    def test_parse_performances(self) -> None:
        expected = [
            'Improve performance of Merge Request List API under load',
            'UpdateMergeRequestsWorker can be expensive ',
            'N+1 issue in epic referenced',
            'Enable snippets to use reference filter cache',
            'Enable labels to use reference filter cache'
            ]
        self.assertListEqual(self.obj.parse_performances(), expected)

    def test_parse_ui_improvements(self) -> None:
        expected = [
            'Group Overview Analytics: Replace metric card with single stat',
            'Display hashes associated with a package',
            'Make “Start/Add Merge Train” button red when the latest pipeline in the merge request has not passed'
            ]
            
        self.assertListEqual(self.obj.parse_ui_improvements(), expected)

    def test_key_improvements(self) -> None:
        expected = [
            'Epic Boards',
            'Terraform module registry built into GitLab',
            'Streamlined top navigation menu',
            'Merge request reviews in VS Code',
            'Sidebar navigation redesign',
            'Edit wiki pages with the WYSIWYG Markdown editor',
            'Aggregate identical DAST vulnerabilities into a single vulnerability',
            'Cluster management project template',
            'Prepopulate the CI/CD pipeline editor with an initial template',
            'Container Scanning Integration with Trivy',
            'Lead time for merge requests at the group level'
        ]
            
        self.assertListEqual(self.obj.parse_key_improvements(), expected)

    def test_improvements(self) -> None:
        expected = [
            'Horizontal navigation for project-level Value Stream Analytics',
            'Improved interface for adding groups to the DevOps Adoption table',
            'SSH key expiration enforced by default',
            'Track usage of Code Owners',
            'Slack notifications for wiki edits include links to diffs',
            'GitLab Runner 14.0',
            'Predefined CI/CD variable for environment action',
            'Install PyPI packages from your group or subgroup',
            'Security report generalized details structure',
            'Feature Flags User List is now on its own page',
            'Dynamically update the Incident Service Level Agreement Timer',
            'Database load balancing moved to Free',
            'Geo support for PostgreSQL high availability in GA',
            'GitLab upgraded to Ruby on Rails 6.1',
            'Performance bar shows how much memory is used',
            'Redesign for Geo sites dashboard',
            'Identify provisioned users at group level',
            'Instance-level DevOps Adoption report enabled by default',
            'Set pronouns on GitLab user profiles',
            'Edit default path and project name when forking',
            'Add ‘~’ to supported characters for CI/CD variable masking',
            'Identify which jobs triggered downstream pipelines',
            'Delete associated package files via UI',
            'Pin to Specific SAST Analyzer Versions',
            'Static Analysis Analyzer Updates',
            'Change an issue’s type',
            'Container Scanning Integration with Grype',
            'Geo requires confirmation before resyncing all projects',
            'GitLab chart improvements',
            'Omnibus improvements',
            'Project storage location available in REST and GraphQL APIs'
        ]
            
        self.assertListEqual(self.obj.parse_improvements(), expected)

    def test_parse_deprecations(self) -> None:
        expected = ['NFS for Git repository storage deprecated']
            
        self.assertListEqual(self.obj.parse_deprecations(), expected)

    def test_parse_removals(self) -> None:
        expected = [
            'Breaking changes to Terraform CI template',
            'Code Quality RuboCop support changed',
            'Container Scanning Engine Clair',
            'DAST environment variable renaming and removal',
            'Default Browser Performance testing job renamed in GitLab 14.0',
            'Default DAST spider begins crawling at target URL',
            'Default branch name for new repositories now main',
            'Deprecated GraphQL fields have been removed',
            'Deprecations for Dependency Scanning',
            'External Pipeline Validation Service Code Changes',
            'Geo Foreign Data Wrapper settings removed',
            'GitLab OAuth implicit grant deprecation',
            'GitLab Runner helper image in GitLab.com Container Registry',
            'GitLab Runner installation to ignore the skel directory',
            'Gitaly Cluster SQL primary elector has been removed',
            'Helm v2 support',
            'Legacy feature flags removed',
            'Legacy storage removed',
            'Limit projects returned in GET /groups/:id/',
            'Make pwsh the default shell for newly-registered Windows Runners',
            'Migrate from SAST_DEFAULT_ANALYZERS to SAST_EXCLUDED_ANALYZERS',
            'New Terraform template version',
            'OpenSUSE Leap 15.1',
            'PostgreSQL 11 support',
            'Removal of deprecated trace parameter from jobs API endpoint',
            'Removal of legacy fields from DAST report',
            'Removal of legacy storage for GitLab Pages',
            'Removal of release description in the Tags API',
            'Removals for License Compliance',
            'Remove DAST default template stages',
            'Remove SAST analyzer SAST_GOSEC_CONFIG variable in favor of custom rulesets',
            'Remove Ubuntu 19.10 (Eoan Ermine) package',
            'Remove /usr/lib/gitlab-runner symlink from package',
            'Remove ?w=1 URL parameter to ignore whitespace changes',
            'Remove FF_RESET_HELPER_IMAGE_ENTRYPOINT feature flag',
            'Remove FF_SHELL_EXECUTOR_USE_LEGACY_PROCESS_KILL feature flag',
            'Remove FF_USE_GO_CLOUD_WITH_CACHE_ARCHIVER feature flag',
            'Remove secret_detection_default_branch job',
            'Remove disk source configuration for GitLab Pages',
            'Remove legacy DAST domain validation',
            'Remove off peak time mode configuration for Docker Machine autoscaling',
            'Remove redundant timestamp field from DORA metrics API payload',
            'Remove success and failure for finished build metric conversion',
            'Remove support for Windows Server 1903 image',
            'Remove support for Windows Server 1909 image',
            'Removed Global SAST_ANALYZER_IMAGE_TAG in SAST CI template',
            'Ruby version changed in Ruby.gitlab-ci.yml',
            'Segments removed from DevOps Adoption API',
            'Service Templates removed',
            'Sidekiq queue selector options no longer accept the ‘experimental’ prefix',
            'Ubuntu 16.04 support',
            'Unicorn removed in favor of Puma for GitLab self-managed',
            'Update Auto Deploy template version',
            'Update CI/CD templates to stop using hardcoded master',
            'WIP merge requests renamed ‘draft merge requests’',
            'Web Application Firewall (WAF)',
            'CI_PROJECT_CONFIG_PATH removed in Gitlab 14.0',
            'CI_PROJECT_CONFIG_PATH variable has been removed'
        ] 

        self.assertListEqual(self.obj.parse_removals(), expected)

    def test_results(self) -> None:
        expected_keys = [
            'key_improvements',
            'improvements',
            'performances',
            'bug_fixes',
            'ui_improvements',
            'deprecations',
            'removals'
        ]
        results = self.obj.results
        self.assertListEqual(list(results.keys()), expected_keys)

if __name__ == '__main__':
    unittest.main()

