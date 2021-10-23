'''Clase para parsear los archivos JSON'''

# Imports
import json
from interfazexception import InterfazException


class JsonParser():
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
            raise InterfazException(self._FILE_NOT_FOUND) from ex
        except json.JSONDecodeError as ex:
            raise InterfazException(self._JSON_decode_error) from ex
        return data

    def _validate_json(self):
        """validate the json keys"""
        for key in self._key_list:
            if not key in self._json_content.keys():
                raise InterfazException(self._key_error_message)

    @property
    def json_content(self):
        """Property for access the json content read from the json file"""
        return self._json_content
