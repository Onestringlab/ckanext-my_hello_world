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
            'hello_world': hello_world_action
        }


def hello_world_action(context, data_dict):
    """
    Fungsi ini akan menangani permintaan ke /api/3/action/hello_world
    """
    # Tambahkan logika untuk mendukung metode GET
    if context.get('method', '').upper() == 'GET':
        return {'message': 'Hello, World! This is a GET request!', 'success': True}
    else:
        raise toolkit.ValidationError('Only GET method is allowed for this endpoint.')
