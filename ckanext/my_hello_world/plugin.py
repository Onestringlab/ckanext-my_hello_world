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
from flask import Blueprint, jsonify

class MyHelloWorldPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)

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
    
    # IRoutes
    def before_map(self, map):
        blueprint = create_blueprint()
        map.connect('welcome', '/welcome', controller=blueprint)
        return map


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
        # packages = Session.query(Package).all()

        # Mengambil dataset yang privat
        # packages = Session.query(Package).filter(Package.private == True).all()

        # Mengambil 10 dataset pertama (paginasi)
        packages = Session.query(Package).limit(10).offset(0).all()
        
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

# Fungsi untuk membuat blueprint Flask
def create_blueprint():
    blueprint = Blueprint('my_hello_world', __name__)

    @blueprint.route('/welcome')
    def welcome():
        """
        Route untuk /welcome
        """
        return jsonify({'message': 'Welcome to CKAN!', 'success': True})

    return blueprint
