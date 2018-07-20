import boto3
import json
import logging
import pytest
from botocore.stub import Stubber


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_event_passes_handler():
    fh = open('tests/mocks/event.json')
    event = json.loads(fh.read())

    import handler

    res = handler.main(event, context={})
