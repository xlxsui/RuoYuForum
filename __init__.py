import os
from flask import Flask, url_for


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='ruoyuforum',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import auth
    app.register_blueprint(auth.bp)

    from . import forum
    app.register_blueprint(forum.bp)
    app.add_url_rule('/', endpoint='index')

    from . import movie
    app.register_blueprint(movie.bp)

    from . import user
    app.register_blueprint(user.bp)

    from . import post
    app.register_blueprint(post.bp)

    app.app_context()
    return app
