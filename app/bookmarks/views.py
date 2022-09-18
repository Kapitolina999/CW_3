from flask import Blueprint, render_template, redirect, abort
import json
import logging

from app.bookmarks.dao.bookmarks import Bookmark
from app.main.dao.posts import Posts

logger = logging.getLogger('basic')

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder='templates')

bookmarks = Bookmark("data/bookmarks.json")
posts = Posts("data/posts.json")


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    try:
        post = posts.get_post_by_pk(post_id)
        bookmarks.add_bookmark(post)
        return redirect('/')
    except ValueError:
        logger.info("добавляются два одинаковых поста")
        return redirect('/')
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    try:
        bookmarks.remove_bookmark(post_id)
        return redirect('/')
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)


@bookmarks_blueprint.route('/bookmarks')
def get_all_bookmarks():
    try:
        all_bookmarks = bookmarks.get_all_bookmarks()
        return render_template('bookmarks.html', bookmarks=all_bookmarks)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)
