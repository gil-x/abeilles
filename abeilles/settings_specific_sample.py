SECRET_KEY = "as you wish"

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

EMAIL_HOST = 'localhost'
EMAIL_USE_TLS = False
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'contact@abeilles-aide-entraide.fr'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SENDINGBLUE_API_KEY = 'you need one'
SENDINGBLUE_SMTP_KEY = 'you need one'
