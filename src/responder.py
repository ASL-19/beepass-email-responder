""" Email Responder Lambda Function """

from log import Log
import hashlib
import api
from botocore.exceptions import ClientError
from pyskoocheh import feedback
from ses import parse_ses_notification
from settings import CONFIG
from template import TEMPLATES
import urllib.parse
import jinja2
from helpers import hash_str


logger = Log("BeePassBot", is_debug=CONFIG['IS_DEBUG'])


def render_template(template, **kwargs):
    ''' renders a Jinja template into HTML '''

    template_loader = jinja2.FileSystemLoader(searchpath="templates/")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template)
    return template.render(
        GET_EMAIL=CONFIG['GET_EMAIL'],
        INSTRUCTION_URL=CONFIG['INSTRUCTION_URL'],
        AWS_BUCKET_STORAGE=CONFIG['AWS_BUCKET_STORAGE'],
        **kwargs)


def email(source_email, template_name):
    try:
        feedback.send_email(
            CONFIG['REPLY_EMAIL'],
            source_email,
            TEMPLATES['EMAIL_SUBJECT'],
            # ToDo: Fix the text format name. It should not be the same for all.
            TEMPLATES['NOSERVER_TEXT_BODY'].format(
                DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            render_template(template_name,
                            DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            '',
            None,
            CONFIG['FEEDBACK_EMAIL'])
        return True
    except ClientError as error:
        logger.error('Error sending email: %s', str(error))
        feedback.send_email(
            CONFIG['REPLY_EMAIL'],
            source_email,
            TEMPLATES['EMAIL_SUBJECT'],
            TEMPLATES['TRY_AGAIN_TEXT_BODY'].format(
                DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            render_template('try_again.j2',
                            DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            '',
            None,
            CONFIG['FEEDBACK_EMAIL'])
        return None


def email_key(source_email, awsurls):
    try:
        feedback.send_email(
            CONFIG['REPLY_EMAIL'],
            source_email,
            TEMPLATES['EMAIL_SUBJECT'],
            TEMPLATES['OUTLINE_NEW_TEXT_BODY'].format(
                DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL'],
                key=awsurls[0]),
            render_template('outline_new.j2',
                            awsurls=awsurls,
                            SUPPORT_EMAIL=CONFIG['SUPPORT_EMAIL'],
                            DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            '',
            None,
            CONFIG['FEEDBACK_EMAIL'])
    except ClientError as error:
        logger.error('Error sending email: %s', str(error))
        feedback.send_email(
            CONFIG['REPLY_EMAIL'],
            source_email,
            TEMPLATES['EMAIL_SUBJECT'],
            TEMPLATES['TRY_AGAIN_TEXT_BODY'].format(
                DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            render_template('try_again.j2',
                            DELETE_USER_EMAIL=CONFIG['DELETE_USER_EMAIL']),
            '',
            None,
            CONFIG['FEEDBACK_EMAIL'])
        return None


def mail_responder(event, _):
    """ Main entry point to handle the feedback form
        event: information about the email
        context: information about the context
    """
    logger.debug('%s: Request received:%s', __name__,
                str(event['Records'][0]['eventSource']))

    try:
        (source_email, recipient) = parse_ses_notification(
            event['Records'][0]['ses'])
    except Exception as exec:
        logger.error(f'Error parsing received Email: {exec}')
        return None

    LANG = CONFIG['LANG']

    logger.debug('Source Email {} recipient {}'.format(
        source_email, recipient))

    if recipient == CONFIG['TEST_EMAIL']:
        feedback.send_email(
            CONFIG['REPLY_EMAIL'],
            source_email,
            TEMPLATES['EMAIL_SUBJECT'],
            'a',
            'a',
            '',
            None,
            CONFIG['FEEDBACK_EMAIL'])
        return True

    elif recipient == CONFIG['TEST_EMAIL_NEW']:
        email_key(source_email, 'https://beepassvpn.com')
        return True

    elif recipient == CONFIG['REPLY_EMAIL']:
        logger.info('Response to no-reply ignored')
        return True

    elif recipient == CONFIG['DELETE_USER_EMAIL']:
        try:
            deleted = api.delete_user(user_id=hash_str(source_email))
        except Exception as exec:
            logger.error(f'Error in deleting user process: {exec}')
            email(source_email, 'try_again.j2')
            return None
        if deleted:
            email(source_email, 'unsubscribed.j2')
            return None

    elif recipient == CONFIG['GET_EMAIL']:
        try:
            user_exist = api.get_user(hash_str(source_email))
        except Exception as exec:
            logger.error('API error when checking {}: {}'.format(
                hash_str(source_email), exec))
            email(source_email, 'try_again.j2')
            return None

        if user_exist:
            email(source_email, 'returning_user.j2')
            return None

        try:
            api.create_user(hash_str(source_email), 'EM')
        except Exception as exec:
            logger.error('API error when Creating {}: {}'.format(
                hash_str(source_email), exec))
            email(source_email, 'try_again.j2')
            return None

        try:
            new_keys, ss_conf_link = api.get_new_key(user_id=hash_str(source_email))
        except Exception as exec:
            logger.error(
                'API error when getting key fo {}: {}'.format(
                    hash_str(source_email), exec))
            email(source_email, 'try_again.j2')
            return None

        if not new_keys or len(new_keys)==0:
            email(source_email, 'no_key.j2')
            return None

        # for index in range(len(new_keys)):
        #     formatted_key = (CONFIG['OUTLINE_AWS_URL']).format(
        #         urllib.parse.quote(new_keys[index]))
        #     new_keys[index] = (f"{formatted_key}#BeePass")
        # online_config_object = api.get_online_config(user_id=hash_str(source_email))
        # online_config_link = f"ssconf://s3.amazonaws.com/{CONFIG['S3_SSCONFIG_BUCKET_NAME']}/{online_config_object['file_name']}.json"

        # ToDo: Simplify this section nad remove new_keys list
        new_keys = [CONFIG['OUTLINE_AWS_URL'].format(
            'fa',
            f"{ss_conf_link}#BeePass")]

        email_key(source_email, new_keys)

    return True
