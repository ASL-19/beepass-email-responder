# coding=UTF8
"""
Settings file for email responder
"""
import logging
import os
# __file__ refers to the file settings.py
CONFIG = {
    'LANG': 'fa',
    'VERSION': '0.0.1',
    # refers to application_top
    'APP_PATH': os.path.dirname(os.path.abspath(__file__)),
    'MAX_ATTACHMENT_SIZE': 500000,    # max size in bytes of attachment
    'IS_DEBUG': '$IS_DEBUG',

    'REGION': $REGION_LIST,

    'TEST_EMAIL': 'test_me@$EMAIL_DOMAIN',
    'TEST_EMAIL_NEW': 'test_me_new@$EMAIL_DOMAIN',
    'DELETE_USER_EMAIL': 'unsubscribe@$EMAIL_DOMAIN',
    'REPLY_EMAIL': 'no-reply@$EMAIL_DOMAIN',
    'GET_EMAIL': 'get@$EMAIL_DOMAIN',
    'FEEDBACK_EMAIL': 'feedback@$EMAIL_DOMAIN',
    'SUPPORT_EMAIL': 'support@$EMAIL_DOMAIN',
    'INSTRUCTION_URL': '$INSTRUCTION_URL',

    'API_KEY': '$API_KEY',
    'API_URL': '$API_URL',
    'API_TIMEOUT': 120,

    'OUTLINE_AWS_URL': 'https://s3.amazonaws.com/$AWS_BUCKET_INVITATION_PAGE/{}/start.html?key={}',
    'S3_SSCONFIG_BUCKET_NAME': '$S3_SSCONFIG_BUCKET_NAME',
    'AWS_BUCKET_STORAGE': '$AWS_BUCKET_STORAGE',
    'OUTLINE_GUIDELINE_PHOTO': {
        'en': 'BeePass-guideline.png',
        'fa': 'BeePass-guideline.png',
        'ar': 'BeePass-guideline-ar.png'
    },
}

API_ENDPOINTS = {
    'ISSUES': '$ISSUES',
    'LIST_USERS': '$LIST_USERS',
    'OUTLINE_KEY': '$OUTLINE_KEY',
    'OUTLINE_CONFIG': '$OUTLINE_CONFIG',
    'REASONS': '$REASONS',
    'SERVERS': '$SERVERS',
    'USERS': '$USERS',
    'USER': '$USER'
}
