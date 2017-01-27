import os
import os.path
import sys

from configobj import ConfigObj
import six
from validate import Validator


context = None

FILE_CONFIG_INI = 'config.ini'
FILE_CONFIG_SPEC_INI = 'configspec.ini'

CONFIG_DIR = os.path.join(sys.prefix, 'config')

config_spec_paths = [
    os.path.join(CONFIG_DIR, FILE_CONFIG_SPEC_INI),
    os.path.abspath(os.path.join('ini', FILE_CONFIG_SPEC_INI))
]

# system-wide
# user (if exists)
# installed
# local dir
config_paths = [
    os.path.join('/etc/dynamicNetworkConfig', FILE_CONFIG_INI),
]

if 'HOME' in os.environ:
    config_paths.append(
        os.path.join(environ['HOME'],
                     '.dynamicNetworkConfig',
                     FILE_CONFIG_INI))

config_paths.append(
    os.path.join(
        CONFIG_DIR,
        FILE_CONFIG_INI
    )
)
config_paths.append(
    os.path.join(
        os.path.abspath(
            os.path.join('ini')
        ),
        FILE_CONFIG_INI
    )
)

CONFIG_SPEC_PATH = None
CONFIG_PATH = None

for spec_path in config_spec_paths:
    if os.path.exists(spec_path):
        CONFIG_SPEC_PATH = spec_path
        break

for config_path in config_paths:
    if os.path.exists(config_path):
        CONFIG_PATH = config_path
        break

if CONFIG_SPEC_PATH is None:
    sys.stderr.write('Unable to find config spec in:')
    for spec_path in config_spec_paths:
        sys.stderr.write(spec_path)

    sys.exit(1)

if CONFIG_PATH is None:
    sys.stderr.write('Unable to find config ini in:')
    for config_path in config_paths:
        sys.stderr.write(config_path)

    sys.exit(1)

config_spec = ConfigObj(os.path.abspath(CONFIG_SPEC_PATH),
                        interpolation=False,
                        list_values=False,
                        _inspec=True)

config = ConfigObj(os.path.abspath(CONFIG_PATH),
                   configspec=config_spec,
                   interpolation=False)

if not config.validate(Validator()):
    raise ValueError('Validation of {0} failed using {1}'
                     .format(CONFIG_PATH,
                             CONFIG_SPEC_PATH))


class Configuration(object):

    def __init__(self, conf_dict=None):
        global config
        if conf_dict is None:
            self.config_dict = config.dict()
        else:
            self.config_dict = conf_dict
        for k, v in six.iteritems(self.config_dict):
            if isinstance(v, dict):
                setattr(self, k, Configuration(conf_dict=v))
            else:
                setattr(self, k, v)


conf = Configuration()
