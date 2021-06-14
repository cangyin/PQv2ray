import collections
import os
import sys

from .utils import load_json


class ConfigError(Exception):
    pass


def load_config(configuration_file):
    """Load a configuration file.
    Args:
        configuration_file (str): name of configuration file.  Name is
        relative to config directory so typically just a file name
        without paths, e.g. "config.json".
    """

    res = None

    for dirname in __config_file_paths():
        print(dirname)
        path = os.path.join(dirname, configuration_file)
        new_config = None
        if os.path.isfile(path):
            new_config = load_json(path)
        if res is None:
            if new_config is None:
                raise ConfigError('Base configuration file %s not found in %s' % (configuration_file, path))
            res = new_config
        elif new_config is not None:
            __update_dict(res, new_config)

    return res


def __config_file_paths():
    """
    Paths in which to look for config files, by increasing order of
    priority (i.e., any config in the last path should take precedence
    over the others).
    """
    return [
        os.path.join('components', 'config'),
        os.path.join(os.environ.get('XDG_CONFIG_HOME',
                     os.path.join(os.path.expanduser('~'), '.config')), 'pqv2ray'),
        os.getcwd()
    ]


def __update_dict(orig, update):
    """Deep update of a dictionary
    For each entry (k, v) in update such that both orig[k] and v are
    dictionaries, orig[k] is recursively updated to v.
    For all other entries (k, v), orig[k] is set to v.
    """
    for (key, value) in update.items():
        if (key in orig and
            isinstance(value, collections.Mapping) and
                isinstance(orig[key], collections.Mapping)):
            __update_dict(orig[key], value)
        else:
            orig[key] = value
