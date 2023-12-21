from typing import Optional, List, Dict, Any
from google.oauth2 import service_account
from googleapiclient.discovery import build, Resource

from .config import GoogleWorkspaceConfig


class GoogleWorkspaceGroupManager:
    """
    Manages Google Workspace groups using Directory API.

    Attributes:
        config (GoogleWorkspaceConfig): Configuration for API access.
    """

    def __init__(self, config: GoogleWorkspaceConfig) -> None:
        self.config = config
        self.service = config.get_service()

    def add_member_to_group(self, group_email: str, member_email: str, role: str) -> Optional[Dict[str, Any]]:
        """
        Adds a member to an existing group with a specified role.

        Args:
            group_email (str): Email address of the group.
            member_email (str): Email address of the member to add.
            role (str): Role to assign ('MEMBER', 'MANAGER', 'OWNER').

        Returns:
            Optional[Dict[str, Any]]: Result of the operation or None if error occurs.
        """
        member = {'email': member_email, 'role': role}
        try:
            return self.service.members().insert(groupKey=group_email, body=member).execute()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_group_info(self, group_email: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves information for a specific group.

        Args:
            group_email (str): Email address of the group.

        Returns:
            Optional[Dict[str, Any]]: Group information or None if error occurs.
        """
        try:
            return self.service.groups().get(groupKey=group_email).execute()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def list_google_workspace_groups(self, your_domain: str) -> Optional[List[Dict[str, Any]]]:
        """
        Lists all groups in the specified Google Workspace domain.

        Args:
            your_domain (str): Google Workspace domain.

        Returns:
            Optional[List[Dict[str, Any]]]: List of groups or None if error occurs.
        """
        try:
            response = self.service.groups().list(domain=your_domain, maxResults=200).execute()
            return response.get('groups', [])
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_group(self, group_email: str, group_name: str, description: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Creates a new group in Google Workspace.

        Args:
            group_email (str): Email for the new group.
            group_name (str): Name for the new group.
            description (Optional[str]): Description of the new group.

        Returns:
            Optional[Dict[str, Any]]: Result of the operation or None if error occurs.
        """
        group_body = {'email': group_email, 'name': group_name, 'description': description}
        try:
            return self.service.groups().insert(body=group_body).execute()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
