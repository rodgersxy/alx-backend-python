#!/usr/bin/env python3
"""
Unittests and Integration Tests
"""
import unittest
import json
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittests for GithubOrgClient
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_public_repos(self, data, mock):
        """
        Test public_repos
        """
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)
