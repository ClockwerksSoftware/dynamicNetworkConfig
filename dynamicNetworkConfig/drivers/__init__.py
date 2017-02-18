import importlib


from dynamicNetworkConfig import config
from dynamicNetworkConfig.drivers.exceptions import (
    BadMetadataDriverException,
)


metadata_driver = None


def do_load_driver(driver_class_name):

    split_position = driver_class_name.rfind('.')
    module_name = driver_class_name[:split_position]
    class_name = driver_class_name[split_position + 1:]

    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def load_driver(driver_type, driver_config, driver_name, driver_exception):
    if hasattr(driver_config, driver_name):
        return do_load_driver(
            getattr(driver_config, driver_name).driver
        )
    else:
        raise driver_exception(
            'Unknown {0} Driver {1}'.format(
                driver_type,
                driver_name
            )
        )


def load_metadata_driver(driver_name):
    return load_driver(
        'Metadata',
        config.metadata_driver,
        driver_name,
        BadMetadataDriverException
    )


def init_model():
    global storage_driver
    global metadata_driver

    storage_driver = load_storage_driver(
        config.storage_driver.driver
    )
    metadata_driver = load_metadata_driver(
        config.metadata_driver.driver
    )
