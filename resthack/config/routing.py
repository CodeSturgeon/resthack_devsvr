"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/mazes/{maze_name}/ascii', controller='veefive',
                action='ascii_dump', conditions=dict(method=['GET', 'HEAD']))
    map.connect('/mazes/{maze_name}/json', controller='veefive',
                action='json_dump', conditions=dict(method=['GET', 'HEAD']))
    map.connect('/avatars/{aid}', controller='veefive', action='pos_get',
                conditions=dict(method=['GET', 'HEAD']))
    map.connect('/avatars/{aid}', controller='veefive', action='pos_post',
                conditions=dict(method=['POST']))

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
