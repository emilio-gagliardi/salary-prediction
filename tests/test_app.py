import pytest
from app.app import *


def yawn():
    return "Yawn"


def test_hello_world():
    assert hello_world() == "Hello World!"
