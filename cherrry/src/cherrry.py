import requests
import json

__version__ = "0.0.1"

URL = "https://api.cherrry.com"

class CherrryClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.table_name = None

    def validate_table(self):
        if self.table_name is None:
            raise Exception("Table not defined: call .table('table_name') first")

    def api_request(self, path, json=None):
        result = None
        error = None
        try:
            result = requests.post(
                URL + path,
                json=json
            )
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if result.text:
                error = str(result.status_code) + " : " + result.text
            else:
                error = e
        except requests.exceptions.RequestException as e:
            error = e

        try:
            result = result.json()
            if path == "/search":
                result = result["result"]
        except requests.exceptions.JSONDecodeError as e:
            result = result.text

        return [result, error]

    def table(self, table_name):
        self.table_name = table_name
        return self

    def create_table(self, table):
        result = self.api_request(
            "/create_table",
            {
                "api_key": self.api_key,
                "name": table
            }
        )
        return result

    def insert(self, data):
        self.validate_table()

        result = self.api_request(
            "/insert",
            {
                "api_key": self.api_key,
                "table": self.table_name,
                "doc": data
            }
        )
        return result

    def search(self, params):
        self.validate_table()

        prompt = params.get("prompt") or ""
        search_type = params.get("search_type") or "text"
        size = params.get("size") or 1

        result = self.api_request(
            "/search",
            {
                "api_key": self.api_key,
                "table": self.table_name,
                "prompt": prompt,
                "size": size,
                "search_type": search_type
            }
        )
        return result

    def doc(self, doc_id):
        self.validate_table()

        result = self.api_request(
            "/doc",
            {
                "api_key": self.api_key,
                "table": self.table_name,
                "doc": doc_id
            }
        )
        return result

    def delete(self, id):
        self.validate_table()

        result = self.api_request(
            "/delete",
            {
                "api_key": self.api_key,
                "table": self.table_name,
                "doc": id
            }
        )
        return result

    def __str__(self):
        data = {"api_key": self.api_key, "table": self.table_name} 
        return json.dumps(data)
