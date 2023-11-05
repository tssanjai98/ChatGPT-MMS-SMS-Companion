from flask import Blueprint, request, jsonify
from flask.views import MethodView
from views.fetchwiki import fetch_wikipedia_content

content_bp = Blueprint('content_bp', __name__)

class ContentFetchView(MethodView):
    def get(self):
        try:
            search_term = request.args.get('topic', '')
            if not search_term:
                return jsonify({'error': 'Search term is required'}), 400

            content = fetch_wikipedia_content(search_term)
            if 'error' in content:
                return jsonify(content), 502

            return jsonify(content)
        except Exception as e:
            return jsonify({'error': f'An error occurred: {e}'}), 500

content_view = ContentFetchView.as_view('content_fetch')
content_bp.add_url_rule('/fetch-content',view_func=content_view)
