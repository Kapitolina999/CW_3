from flask import Blueprint, render_template, jsonify, request, abort
import json
import logging

from app.main.dao.posts import Posts
from app.main.dao.comments import Comments
from app.bookmarks.dao.bookmarks import Bookmark

logger = logging.getLogger('basic')

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts = Posts('data/posts.json')
comments = Comments('data/comments.json')
bookmarks = Bookmark('data/bookmarks.json')


@main_blueprint.route('/')
def all_post():
    logger.debug('Запрошены посты')

    try:
        all_bookmarks = bookmarks.get_all_bookmarks()
        all_posts = posts.get_post_all()
        len_bookmarks = len(all_bookmarks)
        return render_template('index.html', all_post=all_posts, len_bookmarks=len_bookmarks)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)


@main_blueprint.route('/posts/<int:post_id>')
def one_post(post_id):
    logger.debug(f'Запрошен пост {post_id}')

    try:
        post = posts.get_post_by_pk(post_id)
        all_comments = comments.get_comments_by_post_id(post_id)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)
    else:
        if post is None:
            logger.exception("Пост не существует")
            raise FileNotFoundError(f'Пост {post_id} не существует')
    comments_len = len(all_comments)
    return render_template('post.html', comments=all_comments, post=post, comments_len=comments_len)



@main_blueprint.route('/search')
def search_post_by_keyword():
    word = request.args.get('kw')
    try:
        all_posts = posts.search_for_posts(word)
        len_posts = len(all_posts)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)
    else:
        return render_template('search.html', posts=all_posts, len_posts=len_posts)


@main_blueprint.route('/users/<username>')
def search_post_by_username(username):
    try:
        all_posts = posts.get_posts_by_user(username)
        username = username.lower().title()
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)
    else:
        return render_template('user-feed.html', posts=all_posts, username=username)


@main_blueprint.route('/tag/<tag>')
def search_by_tag(tag):
    try:
        all_posts = posts.get_post_by_tag(tag)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден или не удалось преобразовать json")
        abort(404)
    else:
        return render_template("user-feed.html", posts=all_posts)


@main_blueprint.route("/api/posts")
def api_posts():
    all_posts = posts.get_post_all()
    return jsonify(all_posts)


@main_blueprint.route('/api/posts/<int:post_id>')
def api_post_by_post_id(post_id):
    post = posts.get_post_by_pk(post_id)
    return jsonify(post)
