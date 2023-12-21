"""
test_group_manager.py: Unit tests for the GoogleWorkspaceGroupManager class.
"""

import unittest
from unittest.mock import patch, MagicMock
from google_workspace_group_manager import GoogleWorkspaceGroupManager, GoogleWorkspaceConfig


class TestGoogleWorkspaceGroupManager(unittest.TestCase):
    """
    Test cases for GoogleWorkspaceGroupManager class.
    """
    @patch('google.oauth2.service_account.Credentials.from_service_account_file')
    def setUp(self, mock_from_service_account_file):
        """
        Set up test environment for each test method.
        """
        # Mock the credentials and service
        mock_credentials = MagicMock()
        mock_from_service_account_file.return_value = mock_credentials
        mock_scopes = ['https://www.googleapis.com/auth/admin.directory.group']
        self.config = GoogleWorkspaceConfig('path/to/mock/service_account.json', mock_scopes)
        self.group_manager = GoogleWorkspaceGroupManager(self.config)
        self.mock_service = MagicMock()
        self.group_manager.service = self.mock_service

    @patch('google_workspace_group_manager.group_manager.GoogleWorkspaceGroupManager.add_member_to_group')
    def test_add_member_to_group(self, mock_add_member):
        """
        Test adding a member to a group.
        """
        mock_add_member.return_value = {'success': True}
        result = self.group_manager.add_member_to_group('group@example.com', 'member@example.com', 'MEMBER')
        self.assertEqual(result, {'success': True})

    @patch('google_workspace_group_manager.group_manager.GoogleWorkspaceGroupManager.get_group_info')
    def test_get_group_info(self, mock_get_info):
        """
        Test retrieving information about a group.
        """
        mock_get_info.return_value = {'name': 'Test Group', 'email': 'group@example.com'}
        result = self.group_manager.get_group_info('group@example.com')
        self.assertEqual(result, {'name': 'Test Group', 'email': 'group@example.com'})

    @patch('google_workspace_group_manager.group_manager.GoogleWorkspaceGroupManager.list_google_workspace_groups')
    def test_list_google_workspace_groups(self, mock_list_groups):
        """
        Test listing all groups in a domain.
        """
        mock_list_groups.return_value = [{'name': 'Group 1'}, {'name': 'Group 2'}]
        result = self.group_manager.list_google_workspace_groups('example.com')
        self.assertEqual(result, [{'name': 'Group 1'}, {'name': 'Group 2'}])

    @patch('google_workspace_group_manager.group_manager.GoogleWorkspaceGroupManager.create_group')
    def test_create_group(self, mock_create_group):
        """
        Test creating a new group.
        """
        mock_create_group.return_value = {'name': 'New Group', 'email': 'newgroup@example.com'}
        result = self.group_manager.create_group('newgroup@example.com', 'New Group', 'Description')
        self.assertEqual(result, {'name': 'New Group', 'email': 'newgroup@example.com'})


if __name__ == '__main__':
    unittest.main()
