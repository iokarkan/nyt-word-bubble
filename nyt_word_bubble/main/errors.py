from flask import jsonify, request, current_app, url_for, render_template
from . import bp as main

@main.app_errorhandler(404)
def page_not_found(e):

    if (
        request.accept_mimetypes.accept_json
        and not request.accept_mimetypes.accept_html
    ):
        current_app.logger.debug(f"404: Got request accepting JSON only")
        response = jsonify({
            "error": "404: Not found.",
            "message": f"Send a GET request to {url_for('api.hello')} for help."
            })
        response.status_code = 404
        return response

    return "<h1>404</h1>", 404

@main.app_errorhandler(500)
def internal_server_error(e):

    if (
        request.accept_mimetypes.accept_json
        and not request.accept_mimetypes.accept_html
    ):
        current_app.logger.debug(f"500: Internal server error...")
        response = jsonify({
            "error": "500: Internal Server Error.",
            "message": f"Something went wrong. Please contact ioannis.karkanias@gmail.com with details!"
            })
        response.status_code = 500
        return response

    return "<h1>404</h1>", 500
