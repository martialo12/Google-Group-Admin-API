from google.oauth2 import service_account
from googleapiclient.discovery import build, Resource


class GoogleWorkspaceConfig:
    """
    Configuration class for Google Workspace API authentication.

    Attributes:
        service_account_file (str): Path to the service account JSON key file.
        scopes (list[str]): List of scopes required for the API access.
    """

    def __init__(self, service_account_file: str, scopes: list[str]) -> None:
        self.service_account_file = service_account_file
        self.scopes = scopes

    def get_service(self) -> Resource:
        """
        Creates and returns a Google API service resource.

        Returns:
            Resource: Google API service resource.
        """
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_file, scopes=self.scopes
        )
        return build('admin', 'directory_v1', credentials=credentials)
