# Google-Group-Admin-API

A Python library for managing Google Cloud Platform (GCP) groups through the Google Workspace Directory API. This tool allows easy and efficient group management within Google Workspace, including adding members to groups, retrieving group information, listing all groups in a domain, and creating new groups.

## Features

- **Add Members to Groups**: Easily add users to specific Google Workspace groups with designated roles.
- **Get Group Information**: Retrieve detailed information about specific groups.
- **List Groups**: List all groups within a specified Google Workspace domain.
- **Create Groups**: Facilitate the creation of new groups within the Google Workspace.

## Prerequisites

- Python 3.6 or higher
- Google Workspace domain with admin access
- Google Cloud Platform project with the Admin SDK API enabled
- Service account with domain-wide delegation and the necessary permissions

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/[YourGitHubUsername]/Google-Group-Admin-API.git
cd Google-Group-Admin-API

```

## Install the require dependencies

pip install -r requirements.txt


## Usage

First, set up your Google Workspace configuration:

```python
from google_workspace_group_manager import GoogleWorkspaceConfig, GoogleWorkspaceGroupManager

scopes = ['https://www.googleapis.com/auth/admin.directory.group']
config = GoogleWorkspaceConfig('path_to_service_account.json', scopes)
group_manager = GoogleWorkspaceGroupManager(config)
```

### Examples

Adding a member to a group:

```python
group_manager.add_member_to_group('group@example.com', 'member@example.com', 'MEMBER')
```

Retrieving information about a group:

```python
group_info = group_manager.get_group_info('group@example.com')
```

Listing all groups in a domain:

```python
groups = group_manager.list_google_workspace_groups('example.com')
```

Creating a new group:

```python
new_group = group_manager.create_group('newgroup@example.com', 'New Group', 'Description')

```

## Contributing

Contributions are welcome! Please read our Contributing Guide for more information.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- [Google APIs Client Library for Python](https://github.com/googleapis/google-api-python-client)</s>
- [Google Workspace Admin SDK](https://developers.google.com/admin-sdk/directory/v1/guides/manage-groups)</s>
