from flask import Blueprint, request, jsonify
from flask.views import MethodView

index_bp = Blueprint('index_bp', __name__)

class IndexView(MethodView):
    def get(self):
        return jsonify({
            'message': 'This is the homepage'
        })
    
index_view = IndexView.as_view('content_fetch')
index_bp.add_url_rule('/',view_func=index_view)