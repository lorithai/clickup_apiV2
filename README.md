# ClickUp API V2 Client

A Python client for interacting with the ClickUp API V2, providing convenient methods to fetch data, update tasks, and manage custom fields.
Features

* Retrieve team IDs.
* Fetch workspaces, folders, lists, and tasks.
* Get custom fields for a specific list.
* Update task attributes.
* Set custom field values for tasks.

## Installation

pip install 

## Usage
Initialize the Client

```
from clickup_apiV2 import Client 

api_token = "your_clickup_api_token"
client = Client(api_token)
```
## Methods
1. Get Team IDs

Retrieve the IDs of your teams.
```
team_ids = client.get_team_id()
print("Team IDs:", team_ids)
```
2. Get Workspaces

Fetch all workspaces (spaces) for a given team.
```
team_id = "your_team_id"
workspaces = client.get_workspaces(team_id)
print("Workspaces:", workspaces)
```
3. Get Workspace Folders

Fetch all folders within a specific workspace.
```
workspace_id = "your_workspace_id"
folders = client.get_workspace_folders(workspace_id)
print("Folders:", folders)
```
4. Get Workspace Lists

Retrieve lists directly under a workspace.
```
workspace_id = "your_workspace_id"
lists = client.get_workspace_lists(workspace_id)
print("Lists:", lists)
```
5. Get Folder Lists

Fetch lists contained within a folder.
```
folder_id = "your_folder_id"
lists = client.get_folder_lists(folder_id)
print("Folder Lists:", lists)
```
6. Get List Tasks

Retrieve all tasks in a specific list.
```
list_id = "your_list_id"
tasks = client.get_list_tasks(list_id)
print("Tasks:", tasks)
```
7. Get List Custom Fields

Fetch all custom fields for a list.
```
list_id = "your_list_id"
custom_fields = client.get_list_custom_fields(list_id)
print("Custom Fields:", custom_fields)
```
8. Update a Task

Update attributes of a task (e.g., name, status).
```
task_id = "your_task_id"
update_task_data = {
    "name": "New Task Name",
    "status": "in progress"
}
response = client.update_task(task_id, update_task_data)
print("Task Update Response:", response)
```
9. Set Task Custom Field Value

Set or update a custom field value for a task.
```
task_id = "your_task_id"
field_id = "your_field_id"
custom_field_data = {"value": "New Value"}

response = client.set_task_custom_field_value(task_id, field_id, custom_field_data)
print("Set Custom Field Response:", response)
```
# Example Workflow

## Initialize client
```
api_token = "your_clickup_api_token"
client = Client(api_token)
```
## Fetch team IDs
```
team_ids = client.get_team_id()

if team_ids:
    team_id = team_ids[0]
    
    # Get workspaces
    workspaces = client.get_workspaces(team_id)
    print("Workspaces:", workspaces)

    if workspaces:
        workspace_id = workspaces[0]["id"]

        # Get lists in workspace
        lists = client.get_workspace_lists(workspace_id)
        print("Lists:", lists)

        if lists:
            list_id = lists[0]["id"]

            # Get tasks in the list
            tasks = client.get_list_tasks(list_id)
            print("Tasks:", tasks)
            
            if tasks:
                task_id = tasks[0]["id"]

                # Update a task
                update_data = {"status": "completed"}
                client.update_task(task_id, update_data)

                # Set custom field value
                field_id = "your_field_id"
                client.set_task_custom_field_value(task_id, field_id, {"value": "Updated Value"})
```
## Error Handling

The client handles HTTP errors gracefully by catching requests.exceptions.RequestException and printing a relevant error message.

# Contributing

Feel free to submit issues or pull requests to enhance the functionality.

# License

This project is licensed under the MIT License.