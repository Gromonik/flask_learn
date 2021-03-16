from flask import Flask, url_for, request
app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Вывести сообщение с данными id, id - целое число
    return 'Post %s' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug=True)

