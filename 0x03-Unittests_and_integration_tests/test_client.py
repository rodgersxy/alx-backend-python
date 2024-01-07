#!/usr/bin/env python3
"""
this module contains unittests for client
"""
import unittest
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from parameterized import param, parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    unittest to test GithubOrgClient class
    """
    @parameterized.expand([
        param(org_name='google',
              resource="https://api.github.com/orgs/google"),
        param(org_name='abc',
              resource="https://api.github.com/orgs/abc")
    ])
    @patch('client.get_json')
    def test_org(self, mock_getJson, org_name, resource):
        """
        this method should test that GithubOrgClient.org returns the
        correct value
        """
        GithubOrgClient(org_name).org
        mock_getJson.assert_called_once_with(resource)

    def test_public_repos_url(self):
        """
        this method test the public repos url
        should return a known payload
        """
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock
        ) as org_mock:
            org_mock.return_value = {
                "repos_url":  'https://api.github.com/orgs/google/repos'
            }
            res = GithubOrgClient('google').org["repos_url"]
            self.assertEqual(res, 'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_getJson):
        """
        this method unit-test GithubOrgClient.public_repos
        """
        test = [
            {'id': 1, 'name': 'Docker'},
            {'id': 2, 'name': 'Kubernetes'},
            {'id': 2, 'name': 'Github'}
        ]
        mock_getJson.return_value = test
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as public_repos_url_mock:
            public_repos_url_mock.return_value = 'https://github.com/org/abc'
            client0 = GithubOrgClient('abc')
            expected = ['Docker', 'Kubernetes', 'Github']
            self.assertEqual(client0.public_repos(), expected)
            public_repos_url_mock.assert_called_once()
        mock_getJson.assert_called_once()

    @parameterized.expand([
        param(repo={"license": {"key": "my_license"}},
              license_key="my_license", expected=True),
        param(repo={"license": {"key": "other_license"}},
              license_key="my_license", expected=False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        this method tests the has_license function of the Client class
        """
        has_key_bool = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(has_key_bool, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Testing integration
    """
    @classmethod
    def setUpClass(cls):
        """
        set up class before each method
        """
        config = {'return_value.json.side_effect':
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        this method tests public repos with and without license
        """
        testCls = GithubOrgClient('google')
        self.assertEqual(testCls.org, self.org_payload)
        self.assertEqual(testCls.repos_payload, self.repos_payload)
        self.assertEqual(testCls.public_repos(), self.expected_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """tear down after each class"""
        cls.get_patcher.stop()
