"""Class for parsing input JSON Files for the secure_all system"""
import json
from access_management_exception import AccessManagementException


class JsonParser():
    """Class for parsing input JSON Files for the secure_all system"""
    # pylint: disable=too-few-public-methods
    _key_list = []
    _key_error_message = "JSON Decode Error - Wrong label"
    _JSON_decode_error = "JSON Decode Error - Wrong JSON Format"
    _FILE_NOT_FOUND = "Wrong file or file path"

    def __init__(self, file):
        self._file = file
        self._json_content = self._parse_json_file()
        self._validate_json()

    def _parse_json_file(self):
        """read the file in json format format"""
        try:
            with open(self._file, "r", encoding="utf-8", newline="") as json_file:
                data = json.load(json_file)
        except FileNotFoundError as ex:
            raise AccessManagementException(self._FILE_NOT_FOUND) from ex
        except json.JSONDecodeError as ex:
            raise AccessManagementException(self._JSON_decode_error) from ex
        return data

    def _validate_json(self):
        """validate the json keys"""
        for key in self._key_list:
            if not key in self._json_content.keys():
                raise AccessManagementException(self._key_error_message)

    @property
    def json_content(self):
        """Property for access the json content read from the json file"""
        return self._json_content
