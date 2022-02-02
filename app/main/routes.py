import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory, Blueprint, g,current_app, abort
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound
from json                import dumps
from flask_babel         import _, refresh, get_locale

# App modules
from app        import app
from app.forms  import ContactForm
from app.main   import bp
from app.email  import send_contact_form

@bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@bp.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@bp.before_request
def before_request(*args, **kwargs):
    if g.lang_code not in current_app.config['LANGUAGES']:
        adapter = app.url_map.bind('')
        try:
            endpoint, args = adapter.match('/en' + request.full_path.rstrip('/ ?'))
            return redirect(url_for(endpoint, **args), 301)
        except:
            print('Burda cortladın')
            abort(404)
            

    dfl = request.url_rule.defaults
    if 'lang_code' in dfl:
        if dfl['lang_code'] != request.full_path.split('/')[1]:
            print('Hayır Burda cortladın')
            abort(404)


@bp.route('/',methods=['GET', 'POST'])
@bp.route('/index',methods=['GET', 'POST'])
def index():
    form = ContactForm(request.form)
    
    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name =  request.form.get('last_name', '', type=str) 
        contact =  request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

        form_json = {'First Name': str(first_name) ,
                    'Last Name': str(last_name), 
                    'Contact Info': str(contact),
                    'Message': str(message)}

        send_contact_form(form_json)

    return render_template('home/index.html', form=form)

@bp.route('/male-hair-transplant',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/greffe-de-chevuex-pour-homme', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def male_transplant():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

    return render_template('home/male-transplant.html',form=form)

@bp.route('/female-hair-transplant',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/greffe-de-chevuex-pour-femme', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def female_transplant():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

    return render_template('home/female-transplant.html',form=form)

@bp.route('/facial-hair-transplant',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/greffe-de-barbe', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def facial_transplant():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)



    return render_template('home/facial-transplant.html',form=form)

@bp.route('/eyebrow-transplant',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/greffe-de-sourcils', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def eyebrow_transplant():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

    return render_template('home/eyebrow-transplant.html',form=form)

@bp.route('/transplant-methods',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/méthodes-de-transplantation', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def transplant_methods():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

    return render_template('home/transplant-methods.html',form=form)

@bp.route('/our-partners',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/nos-partenaires', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def our_partners():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)

    return render_template('home/our-partners.html',form=form)

@bp.route('/about-us',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/a-propos-de-nous', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def about():
    return render_template('home/about.html')

@bp.route('/contact-us',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/contactez-nous', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def contact():
    return render_template('home/about.html')

@bp.route('/our-services',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/nos-services', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def services():
    return render_template('home/about.html')

@bp.route('/packages',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/packages', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def packages():
    return render_template('home/about.html')

@bp.route('/experience',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/experiences', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def experience():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        first_name = request.form.get('first_name', '', type=str)
        last_name = request.form.get('last_name', '', type=str) 
        phone_number = request.form.get('phone', '', type=str) 
        message = request.form.get('message', '', type=str)
         
    return render_template('home/experience.html',form=form)

@bp.route('/faq',defaults={'lang_code': 'en'},methods=['GET', 'POST'])
@bp.route('/faq', defaults={'lang_code': 'fr'},methods=['GET', 'POST'])
def faq():
    return render_template('home/about.html')


