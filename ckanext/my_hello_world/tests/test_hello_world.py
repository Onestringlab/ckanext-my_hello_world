import pytest
from ckan.plugins.toolkit import get_action


def test_hello_world_action(app_config, mocker):
    """
    Pengujian unit untuk endpoint hello_world
    """
    # Mock context dan data_dict
    context = {}
    data_dict = {}

    # Panggil action
    action = get_action('hello_world')
    result = action(context, data_dict)

    # Validasi hasil
    assert result['message'] == 'Hello, World!'
    assert result['success'] is True
