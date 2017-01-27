import json

from dynamicNetworkConfig.transport.wsgi import errors
from dynamicNetworkConfig.model import json_model


def get_json(request, command):
    length = request.content_length

    if not length:
        raise errors.NoDataError(
            "Request had no body content"
        )

    raw_data = request.stream.read(length)
    if len(raw_data) != length:
        raise errors.TooLittleDataError(
            "Read {0} bytes when expecting {1} bytes".format(
                len(raw_data),
                length
            )
        )

    try:
        decoded_data = raw_data.decode()
    except Exception as ex:
        raise errors.UnableToDecodeDataError(
            "Unable to decode data: {0}".format(
                ex
            )
        )

    try:
        json_data = json.loads(
            decoded_data
        )
    except Exception as ex:
        raise errors.InvalidJsonError(
            "Message body is malformed: {0}".format(
                ex
            )
        )

    return json_model.JsonModel(json_data, command)
