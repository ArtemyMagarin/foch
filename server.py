from bottle import route, request, response, run, template, static_file, view, error, redirect, TEMPLATES
from Users import User


@route('/')
def index():
    uid = request.get_cookie('uid', secret='uid')
    if uid:
        redirect('/account/'+str(uid))
    else:
        redirect('/login')



@route('/login', method='GET')
def login():
    return template('login', pass_valid=True, login='')

@route('/login', method='POST')
def login():
    login = request.forms.get('login')
    password = request.forms.get('password')
    user = User()
    uid = user.check_password(login, password)
    if uid:
        response.set_cookie('uid', uid, secret="uid")
        redirect('/account/'+str(uid)) 
    return template('login', pass_valid=False, login=login)

@route('/signin', method='GET')
def signin():
    return template('signin', username='', email='', error_msg='')

@route('/signin', method='POST')
def signin():
    username = request.forms.get('login')
    password = request.forms.get('password')
    email = request.forms.get('email')
    user = User()
    try:
        user.new_user(username, email, password)
    except Exception as e:
        return template('signin', username=username, email=email, error_msg=str(e))
    redirect('/')


@route('/account/<uid>')
def show_account(uid):
    return uid

@route('/logout')
def logout():
    response.delete_cookie('uid')
    redirect('/')


# static files:
@route('/static/images/<pic:re:.*\.png>')
def serve_pictures(pic):
    return static_file(pic, root='static/images')

@route('/<page:re:.*\.html>')
def serve_html(page):
    if page == 'index.html':
        redirect('/')
    return static_file(page, root='static/pages')



# errors:
@error(404)
def error404(error):
    return static_file("404.html", root='errors')



run(host='localhost', port=8080, debug=True)
