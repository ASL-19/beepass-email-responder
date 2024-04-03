from pyskoocheh.errors import ValidationError


def parse_ses_notification(ses_notification):
    """ Gather incoming email info and validate

    Args:
        ses_notification: ses object from Lambda event
    Returns:
        source_email, recipient
    """
    if ses_notification['receipt']['spamVerdict']['status'] == 'FAIL':
        raise ValidationError('Email flagged as spam. EMAIL={}'.format(
            ses_notification['mail']['source']))

    if ses_notification['receipt']['virusVerdict']['status'] == 'FAIL':
        raise ValidationError('Email contains virus. EMAIL={}'.format(
            ses_notification['mail']['source']))

    source_email = ses_notification['mail']['source']
    recipient = ses_notification['mail']['destination'][0].lower()
    return (source_email, recipient)
