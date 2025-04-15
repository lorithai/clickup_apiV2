import pytest
from unittest.mock import patch, Mock
from clickup_apiv2.client import Client

API_TOKEN = "dummy_token"

class TestClient:
    def setup_method(self):
        self.client = Client(API_TOKEN)

    @patch("clickup_apiv2.client.requests.get")
    def test_get_workspace_folders(self, mock_get):
        mock_get.return_value = self._mock_json_response({"folders": [{"id": "f1", "name": "Folder 1"}]})
        folders = self.client.get_workspace_folders("123")
        assert folders == [{"id": "f1", "name": "Folder 1"}]

    @patch("clickup_apiv2.client.requests.get")
    def test_get_workspace_lists(self, mock_get):
        mock_get.return_value = self._mock_json_response({"lists": [{"id": "l1", "name": "List 1"}]})
        lists = self.client.get_workspace_lists("456")
        assert lists == [{"id": "l1", "name": "List 1"}]

    @patch("clickup_apiv2.client.requests.get")
    def test_get_folder_lists(self, mock_get):
        mock_get.return_value = self._mock_json_response({"lists": [{"id": "l2", "name": "Folder List"}]})
        lists = self.client.get_folder_lists("789")
        assert lists == [{"id": "l2", "name": "Folder List"}]

    @patch("clickup_apiv2.client.requests.get")
    def test_get_list_tasks(self, mock_get):
        mock_get.return_value = self._mock_json_response({
            "tasks": [{"id": "t1", "name": "Task 1", "status": {"status": "open"}}]
        })
        tasks, data = self.client.get_list_tasks("list1")
        assert tasks[0]["status"] == "open"

    @patch("clickup_apiv2.client.requests.get")
    def test_get_list_custom_fields(self, mock_get):
        mock_get.return_value = self._mock_json_response({
            "fields": [{"id": "cf1", "name": "Field"}]
        })
        fields = self.client.get_list_custom_fields("list2")
        assert fields[0]["id"] == "cf1"

    @patch("clickup_apiv2.client.requests.put")
    def test_update_task(self, mock_put):
        mock_put.return_value = self._mock_json_response({"updated": True})
        result = self.client.update_task("task1", {"name": "Updated Task"})
        assert result["updated"] is True

    @patch("clickup_apiv2.client.requests.post")
    def test_set_task_custom_field_value(self, mock_post):
        mock_post.return_value = self._mock_json_response({"success": True})
        result = self.client.set_task_custom_field_value("task1", "field1", {"value": "new"})
        assert result["success"]

    @patch("clickup_apiv2.client.requests.post")
    def test_create_task(self, mock_post):
        mock_post.return_value = self._mock_json_response({"id": "task2", "name": "Created Task"})
        result = self.client.create_task("list3", "Created Task", {})
        assert result["id"] == "task2"

    @patch("clickup_apiv2.client.requests.delete")
    def test_delete_task(self, mock_delete):
        mock_delete.return_value = self._mock_json_response({"deleted": True})
        result = self.client.delete_task("task2")
        assert result["deleted"]

    @patch("clickup_apiv2.client.requests.post")
    def test_set_custom_field_value(self, mock_post):
        mock_post.return_value = self._mock_json_response({"value_set": True})
        result = self.client.set_custom_field_value("task3", "field2", "123")
        assert result["value_set"]

    def _mock_json_response(self, json_data):
        mock_resp = Mock()
        mock_resp.json.return_value = json_data
        mock_resp.raise_for_status.return_value = None
        return mock_resp