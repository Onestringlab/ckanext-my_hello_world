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
from flask import Blueprint, Response


class MyHelloWorldPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'my_hello_world')

    # IRoutes
    def get_blueprint(self):
        blueprint = Blueprint('hello_world', __name__)

        @blueprint.route('/hello')
        def hello_world():
            return Response("Hello, World!", mimetype='text/plain')

        return blueprint
