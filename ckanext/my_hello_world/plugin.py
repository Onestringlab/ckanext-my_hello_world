# import ckan.plugins as plugins
# import ckan.plugins.toolkit as toolkit


# class MyHelloWorldPlugin(plugins.SingletonPlugin):
#     plugins.implements(plugins.IConfigurer)

#     # IConfigurer

#     def update_config(self, config_):
#         toolkit.add_template_directory(config_, 'templates')
#         toolkit.add_public_directory(config_, 'public')
#         toolkit.add_resource('fanstatic',
#             'my_hello_world')


import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MyHelloWorldPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'my_hello_world')

    # IActions
    def get_actions(self):
        return {
            'hello_world': hello_world_action,
            'goodbye_world': goodbye_world_action
        }


def hello_world_action(context, data_dict):
    """
    Menangani permintaan ke /api/3/action/hello_world
    """
    return {
        'message': 'Hello, World! This is a POST request!',
        'success': True,
        'method': toolkit.request.method
    }


def goodbye_world_action(context, data_dict):
    """
    Menangani permintaan ke /api/3/action/goodbye_world
    """
    return {
        'message': 'Goodbye, World! This is another POST request! Yeay!',
        'success': True,
        'method': toolkit.request.method
    }
