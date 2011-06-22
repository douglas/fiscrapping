from settings import MIDDLEWARE_CLASSES, INSTALLED_APPS, PROJECT_ROOT

import os

INSTALLED_APPS = list(INSTALLED_APPS)
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)

# Django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.extend(['debug_toolbar', 'debug_toolbar_htmltidy'])
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'minha_grade.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
