WTF_CSRF_ENABLED = True # activates the cross-site request forgery prevention and it is enabled by default flask-WTF
SECRET_KEY = 'you-will-never-guess' # only needed when CSRF is enabled , used to create cryptographic token that is used to validate forms

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]



