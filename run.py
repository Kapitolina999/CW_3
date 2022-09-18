from flask import Flask

from logger import create_logger
from app.main.views import main_blueprint
from app.bookmarks.views import bookmarks_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

create_logger()

app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
