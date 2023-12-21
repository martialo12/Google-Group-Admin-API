"""
This script demonstrates the usage of the Google-Group-Admin-API library.

It includes examples of how to add a member to a group, retrieve group information,
list all groups in a domain, and create a new group.
"""

from google_workspace_group_manager import GoogleWorkspaceGroupManager, GoogleWorkspaceConfig

def main():
    """
    Main function to demonstrate the usage of the Google-Group-Admin-API library.
    """
    # Configuration setup
    service_account_file = 'path_to_service_account.json'
    scopes = ['https://www.googleapis.com/auth/admin.directory.group']
    config = GoogleWorkspaceConfig(service_account_file, scopes)
    group_manager = GoogleWorkspaceGroupManager(config)

    # Example domain and group details
    example_domain = 'example.com'
    example_group_email = 'group@example.com'
    example_member_email = 'member@example.com'

    # Add a member to a group
    add_member_result = group_manager.add_member_to_group(example_group_email, example_member_email, 'MEMBER')
    print("Add Member Result:", add_member_result)

    # Retrieve group information
    group_info = group_manager.get_group_info(example_group_email)
    print("Group Info:", group_info)

    # List all groups in a domain
    groups_list = group_manager.list_google_workspace_groups(example_domain)
    print("Groups in Domain:", groups_list)

    # Create a new group
    new_group_info = group_manager.create_group('newgroup@example.com', 'New Group', 'Group Description')
    print("New Group Info:", new_group_info)

if __name__ == "__main__":
    main()
