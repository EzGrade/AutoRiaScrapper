def setup_django():
    import os
    import sys
    import dotenv
    dotenv.load_dotenv()

    import django.conf

    current_dir = os.path.dirname(os.path.abspath(__file__))
    django_dir = os.path.join(current_dir, 'AutoRia')
    sys.path.append(django_dir)

    if not django.conf.settings.configured:
        django.conf.settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': os.environ.get("DATABASE_NAME"),
                    'USER': os.environ.get("DATABASE_USER"),
                    'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
                    'HOST': os.environ.get("DATABASE_HOST"),
                    'PORT': os.environ.get("DATABASE_PORT"),
                }
            },
            INSTALLED_APPS=[
                'rest_framework',
                'ticket.apps.TicketConfig',
            ]
        )
        django.setup()
