from datetime import timedelta


class Config:
    SECRET_KEY = "5791628bb0b13ce0c676dfde280ba245"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "<gmail username>"
    MAIL_PASSWORD = '<gmail password>'
    JWT_SECRET_KEY = SECRET_KEY
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=1)
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 10


