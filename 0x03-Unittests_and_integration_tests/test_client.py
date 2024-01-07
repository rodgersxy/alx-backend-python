import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        expected_response = {
            'login': org_name, 'name': f'Mocked {org_name} Organization'}
        mock_get_json.return_value = expected_response

        github_org_client = GithubOrgClient(org_name)

        org_info = github_org_client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(org_info, expected_response)


if __name__ == "__main__":
    unittest.main()
