
from config.project_configs import PROJECT_CONFIGS

USE_EXTERNAL_LOGGER: bool = PROJECT_CONFIGS.get("USE_EXTERNAL_LOGGER").lower() == 'true'

if USE_EXTERNAL_LOGGER:
    CUSTOM_LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'external': {
                'level': 'DEBUG',
                'class': 'utils.logger.logger_handler.CustomExternalHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['external'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
else:
    # Default Django logging configuration
    CUSTOM_LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{asctime} {levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'debug_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'logs/debug.log',
                'formatter': 'verbose',
            },
            'info_file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'logs/info.log',
                'formatter': 'verbose',
            },
            'error_file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': 'logs/error.log',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['debug_file', 'info_file', 'error_file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

