from flask import Blueprint, request, render_template, url_for

main_blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main_blueprint.route('/')
def main():
    return render_template('index.html')

