class Basic:

    SQLALCHEMY_DATABASE_URI = 'dialect+driver://username:password \
                                @host:port/database'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_RECORD_QUERIES = True


class Development(Basic):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Komorebi.@49.232.161.245:3306/motto'


class Production(Basic):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False


config = {
    'development': Development,
    'product': Production
}
