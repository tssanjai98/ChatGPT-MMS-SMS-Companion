from flask import Flask
from flask import Blueprint
from views.fetchcontent_view import content_bp
from views.index_view import index_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(content_bp)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port='3000')