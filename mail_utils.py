# -*- coding:utf-8 -*-
# coding=<utf8>

from django.core.mail import EmailMultiAlternatives
from djlib.text_utils import htmlize
from django.conf import settings


def send_email_html(subject, message_html, to, fio=''):
    if settings.EMAIL_HOST_USER:
        good_mails = [mail for mail in to if mail != '']
        from_email = "meoc-it@mail.ru"
        # text_content = 'This is an important message.'
        # html_content =
        # '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, message_html,
                                     from_email, good_mails)
        msg.attach_alternative(message_html, "text/html")
        msg.send()
    else:
        pass


def send_email_alternative(subject, message, to, fio=''):
    if settings.EMAIL_HOST_USER:
        message_html = htmlize(message)
        good_mails = [mail for mail in to if mail != '']
        from_email = "meoc-it@mail.ru"
        # text_content = 'This is an important message.'
        # html_content =
        # '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, message, from_email,
                                     good_mails)
        msg.attach_alternative(message_html, "text/html")
        msg.send()
    else:
        pass
