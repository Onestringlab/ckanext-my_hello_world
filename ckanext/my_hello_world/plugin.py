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
from ckan.model import Package
from ckan.model.meta import Session

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
            'get_packages': get_packages_action
        }


def hello_world_action(context, data_dict):
    """
    Endpoint sederhana
    """
    return {'message': 'Hello, World!', 'success': True}


def get_packages_action(context, data_dict):
    """
    Mengambil data paket dari database menggunakan SQLAlchemy
    """
    try:
        # Query semua paket dari tabel package
        packages = Session.query(Package).all()
        
        # Mapping hasil query ke dalam format JSON-friendly
        package_list = [
            {
                'id': pkg.id,
                'name': pkg.name,
                'title': pkg.title,
                'private': pkg.private
            }
            for pkg in packages
        ]
        
        return {'success': True, 'data': package_list}
    except Exception as e:
        raise toolkit.ValidationError(f'Error fetching data: {str(e)}')
