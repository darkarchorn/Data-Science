from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from .routes.human_routes import human_bp
    app.register_blueprint(human_bp)

    return app
