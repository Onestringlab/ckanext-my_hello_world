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


from ckan.plugins import SingletonPlugin, implements
from ckan.plugins.toolkit import IActions, response_json

class HelloWorldPlugin(SingletonPlugin):
    """
    Plugin sederhana untuk menambahkan API baru bernama 'hello_world'
    """
    implements(IActions)

    def get_actions(self):
        # Tambahkan aksi API baru bernama 'hello_world'
        return {
            'hello_world': hello_world
        }

def hello_world(context, data_dict):
    """
    Aksi API sederhana yang mengembalikan pesan
    """
    # Ambil parameter 'name' jika ada
    name = data_dict.get('name', 'World')
    return {'message': f'Hello, {name}!'}
