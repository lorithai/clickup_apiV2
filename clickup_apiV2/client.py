import requests

class Client:
    def __init__(self,api_token):
        self.server = "https://api.clickup.com"
        self.api_token = api_token


    def get_team_id(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
            }

        url = f"{self.server}/api/v2/team"
        try:
            # Make the GET request
            response = requests.get(url, headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Return the team ID(s) from the response
            team_ids = [team['id'] for team in data.get('teams', [])]
            return team_ids
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_workspaces(self, team_id):
        url = f"{self.server}/api/v2/team/{team_id}/space"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the GET request
            response = requests.get(url, headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Extract and return the workspace (space) details
            workspaces = [{"id": space["id"], "name": space["name"]} for space in data.get("spaces", [])]
            return workspaces
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching workspaces: {e}")
            return None
    
    def get_workspace_folders(self, workspace_id):
        url = f"{self.server}/api/v2/space/{workspace_id}/folder"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            folders = [{"id": folder["id"], "name": folder["name"]} for folder in data.get("folders", [])]
            return folders
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching folders: {e}")
            return None

    def get_workspace_lists(self, workspace_id):
        url = f"{self.server}/api/v2/space/{workspace_id}/list"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            lists = [{"id": lst["id"], "name": lst["name"]} for lst in data.get("lists", [])]
            return lists
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching lists: {e}")
            return None

    def get_folder_lists(self, folder_id):
        url = f"{self.server}/api/v2/folder/{folder_id}/list"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            lists = [{"id": lst["id"], "name": lst["name"]} for lst in data.get("lists", [])]
            return lists
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching folder lists: {e}")
            return None

    def get_list_tasks(self, list_id):
        url = f"{self.server}/api/v2/list/{list_id}/task"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            tasks = [{"id": task["id"], "name": task["name"], "status": task.get("status", {}).get("status")} for task in data.get("tasks", [])]
            return tasks
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching tasks: {e}")
            return None

    def get_list_custom_fields(self, list_id):
        url = f"{self.server}/api/v2/list/{list_id}/field"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            custom_fields = [{"id": field["id"], "name": field["name"], "type": field.get("type")} for field in data.get("fields", [])]
            return custom_fields
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching custom fields: {e}")
            return None


    def update_task(self, task_id,update_task_data):
        url = f"{self.server}/api/v2/task/{task_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the PUT request with custom_field_data in the JSON payload
            response = requests.put(url, headers=headers, json=update_task_data)
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating custom field: {e}")
            return None

    def set_task_custom_field_value(self,task_id,field_id,custom_field_data):
        url = f"{self.server}/api/v2/task/{task_id}/field/{field_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the PUT request with custom_field_data in the JSON payload
            response = requests.post(url, headers=headers, json=custom_field_data)
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating custom field: {e}")
            return None


"""
    def get_workspace_folders(self,workspace_id):
        url = f"{self.server}/api/v2/space/{workspace_id}/folder"

    def get_workspace_lists(self,workspace_id):
        url = f"{self.server}/api/v2/space/{workspace_id}/list"

    def get_folder_lists(self,folder_id):
        url = f"{self.server}/api/v2/folder/{folder_id}/list"

    def get_list_tasks(self,list_id):
        url = f"{self.server}/api/v2/list/{list_id}/task"

    def get_list_custom_fields(self,list_id):
        url = f"{self.server}/api/v2/list/{list_id}/field"

    def create_task(self,list_id):
        url = f"{self.server}/api/v2/list/{list_id}/task"

    def set_task_custom_field_value(self,task_id,field_id):
        pass
"""