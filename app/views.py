import os

# Flask modules
from flask      import url_for, redirect, send_from_directory, g, request
from app        import app

@app.route('/')
def home():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('bp.index'))
    
# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')


@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt')

# provide login manager with load_user callback
# @lm.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))

# Logout user
# @app.route('/logout.html')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# # Register a new user
# @app.route('/register.html', methods=['GET', 'POST'])
# def register():
    
#     # declare the Registration Form
#     form = RegisterForm(request.form)

#     msg     = None
#     success = False

#     if request.method == 'GET': 

#         return render_template( 'accounts/register.html', form=form, msg=msg )

#     # check if both http method is POST and form is valid on submit
#     if form.validate_on_submit():

#         # assign form data to variables
#         username = request.form.get('username', '', type=str)
#         password = request.form.get('password', '', type=str) 
#         email    = request.form.get('email'   , '', type=str) 

#         # filter User out of database through username
#         user = Users.query.filter_by(user=username).first()

#         # filter User out of database through username
#         user_by_email = Users.query.filter_by(email=email).first()

#         if user or user_by_email:
#             msg = 'Error: User exists!'
        
#         else:         

#             pw_hash = bc.generate_password_hash(password)

#             user = Users(username, email, pw_hash)

#             user.save()

#             msg     = 'User created successfully.'     
#             success = True

#     else:
#         msg = 'Input error'     

#     return render_template( 'accounts/register.html', form=form, msg=msg, success=success )

# # Authenticate user
# @app.route('/login.html', methods=['GET', 'POST'])
# def login():
    
#     # Declare the login form
#     form = LoginForm(request.form)

#     # Flask message injected into the page, in case of any errors
#     msg = None

#     # check if both http method is POST and form is valid on submit
#     if form.validate_on_submit():

#         # assign form data to variables
#         username = request.form.get('username', '', type=str)
#         password = request.form.get('password', '', type=str) 

#         # filter User out of database through username
#         user = Users.query.filter_by(user=username).first()

#         if user:
            
#             if bc.check_password_hash(user.password, password):
#                 login_user(user)
#                 return redirect(url_for('index'))
#             else:
#                 msg = "Wrong password. Please try again."
#         else:
#             msg = "Unknown user"

#     return render_template( 'accounts/login.html', form=form, msg=msg )

# App main route + generic routing
# @app.route('/', defaults={'path': 'index.html'}, methods=['GET', 'POST'])
