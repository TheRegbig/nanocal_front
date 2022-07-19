import json
from constants import *


class Params:
    def __init__(self):
        self.tango_host = "lid13ctrl1.esrf.fr:20000"
        self.device_proxy = "ID13/NanoControl/1"

        self.http_host = "http://160.103.33.50:8000/"

        self.calib_path = "./settings/calibration.json"
        self.data_path = "./data/"

    def __str__(self):
        return str(vars(self))

class Settings:
    """Reads a JSON configuration file."""

    def __init__(self, path: str):
        """Initializes dictionary.

        Args:
            path: A string path to JSON file.

        Raises:
            ValueError if file doesn't exist or has invalid extension or is empty.
        """
        self._json = dict()
        if not os.path.exists(path):
            raise ValueError("Settings file doesn't exist.")
        if not os.path.splitext(path)[-1] != JSON_EXTENSION:
            raise ValueError("Settings file doesn't have '{}' extension.".format(JSON_EXTENSION))
        with open(path, 'r') as f:
            self._json = json.load(f)
        if not self._json:
            raise ValueError("Empty settings file defined.")

    def json(self):
        """Provides access to the read dictionary."""
        return self._json


class SettingsParser:
    """Parses configuration file with all necessary acquisition parameters."""

    def __init__(self, path: str):
        """Initializes dictionary and checks that all needed fields exist.

        After correct parsing it is possible to obtain ???? AM: add description.

        Args:
            path: A string path to JSON file.

        Raises:
            ValueError if any field doesn't exist.
        """
        json_dict = Settings(path).json()
        if SETTINGS_FIELD not in json_dict:
            raise ValueError("No '{}' field found in the settings file.".format(SETTINGS_FIELD))
        else:
            self._settings_dict = json_dict[SETTINGS_FIELD]
            for field in [TANGO_FIELD, HTTP_FIELD, PATHS_FIELD]:
                if field not in self._settings_dict:
                    raise ValueError("No '{}' field found in the settings file.".format(field))

        self._invalid_fields = []
        # only in that order
        self._parse_params()
        self._check_invalid_fields()

    def get_params(self) -> Params:
        """Provides explicit access to the read TangoParams."""
        return self._params

    def _parse_params(self):
        """Parses all necessary parameters and fills instance."""
        self._params = Params()

        for field in [TANGO_HOST_FIELD, DEVICE_PROXY_FIELD]:
            if field not in self._settings_dict[TANGO_FIELD] or \
                not isinstance(self._settings_dict[TANGO_FIELD][field], str):
                self._invalid_fields.append(field)

        for field in [HTTP_HOST]:
            if field not in self._settings_dict[HTTP_FIELD] or \
                not isinstance(self._settings_dict[HTTP_FIELD][field], str):
                self._invalid_fields.append(field)

        for field in [CALIB_PATH_FIELD, DATA_PATH_FIELD]:
            if field not in self._settings_dict[PATHS_FIELD] or \
                not isinstance(self._settings_dict[PATHS_FIELD][field], str):
                self._invalid_fields.append(field)

        self._params.tango_host = self._settings_dict[TANGO_FIELD][TANGO_HOST_FIELD]
        self._params.device_proxy = self._settings_dict[TANGO_FIELD][DEVICE_PROXY_FIELD]

        self._params.http_host = self._settings_dict[HTTP_FIELD][HTTP_HOST]

        self._params.calib_path = self._settings_dict[PATHS_FIELD][CALIB_PATH_FIELD]
        self._params.data_path = self._settings_dict[PATHS_FIELD][DATA_PATH_FIELD]

    def _check_invalid_fields(self):
        """Raises ValueError if at least one required field is missing in the settings."""
        if self._invalid_fields:
            invalid_fields_str = ", ".join(self._invalid_fields)
            raise ValueError("Wrong or missing inputs in the settings file: {}.".format(invalid_fields_str))


if __name__ == '__main__':
    try:
        _path = "./settings/settings.json"
        parser = SettingsParser(_path)
        params = parser.get_params()

    except BaseException as e:
        print(e)
