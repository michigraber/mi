
# local settings
# this might override previous definitions

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'michigraber$mi',               # Or path to database file if using sqlite3.
        'USER': 'michigraber',                  # Not used with sqlite3.
        'PASSWORD': 'antigone',                 # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    },
}

