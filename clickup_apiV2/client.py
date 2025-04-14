import requests

class Client:
    def __init__(self,api_token):
        self.server = "https://api.clickup.com"
        self.api_token = api_token


    def get_team_id(self,response="full"):
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
            if response == "short":
                team_ids = [team['id'] for team in data.get('teams', [])]
                return team_ids
            else:
                return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_workspaces(self, team_id,response="full"):
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
            if response == "short":
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
            return tasks, data
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

    def create_task(self,list_id,task_name,payload={},custom_task_ids=False,team_id=None):
        """
        example payload (https://developer.clickup.com/reference/createtask)
        payload = {
            "assignees": [1, 2],
            "name": "hello",
            "description": "asdf",
            "archived": True,
            "group_assignees": ["dd01f92f-48ca-446d-88a1-0beb0e8f5f14"],
            "tags": ["tag1"],
            "status": "Open",
            "priority": 2,
            "due_date": 1508369194377,
            "time_estimate": 8640000,
            "due_date_time": True,
            "start_date": 1567780450202,
            "start_date_time": True,
            "points": 2,
            "notify_all": False,
            "parent": None,
            "links_to": None,
            "check_required_custom_fields": True
        }
        """
        url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        data = {"name":task_name,
                   }
        data = data | payload

        try:
            # Make the PUT request with data in the JSON payload
            response = requests.post(url, headers=headers, json=data)
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while creating task: {e}")
            return None

    def delete_task(self,task_id):

        url = f"https://api.clickup.com/api/v2/task/{task_id}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the PUT request with data in the JSON payload
            response = requests.delete(url, headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while deleting task: {e}")
            return None

    def set_custom_field_value(self,task_id,field_id,value):
        url = f"https://api.clickup.com/api/v2/task/{task_id}/field/{field_id}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        payload={"value":value}
        try:
            # Make the PUT request with data in the JSON payload
            response = requests.post(url,json=payload, headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while setting custom field: {e}")
            return None

    def get_current_timer(self, team_id, assignee=None):
        url = f"https://api.clickup.com/api/v2/team/{team_id}/time_entries/current"
        if assignee:
            url += f"?assignee={assignee}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the PUT request with data in the JSON payload
            response = requests.get(url,headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while setting custom field: {e}")
            return None

    def get_time_entries(self, team_id, query_string=None):
        # https://developer.clickup.com/reference/gettimeentrieswithinadaterange
        url = f"https://api.clickup.com/api/v2/team/{team_id}/time_entries"
        if query_string:
            url += f"?{query_string}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.api_token
        }
        try:
            # Make the PUT request with data in the JSON payload
            response = requests.get(url,headers=headers)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            # Return the response data or success message
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while setting custom field: {e}")
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
