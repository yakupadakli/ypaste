from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template.context import Context
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from paste.utils import highlighter_without_number_helper

from ypaste import settings


class EmailService(object):

    def __init__(self):
        self.no_reply_email = getattr(settings, "NO_REPLY_EMAIL", "")
        self.from_email = self.no_reply_email
        self.from_name = getattr(settings, "FROM_NAME", "")

    def send_mail(self, subject, recipient_list, template_body, from_email=None, from_name=None):
        from_email = "%s <%s>" % (
            from_name if from_name else self.from_name, from_email if from_email else self.from_email
        )
        mail = EmailMultiAlternatives(
          subject=subject,
          body=template_body,
          from_email=from_email,
          to=recipient_list,
          headers={"Reply-To": self.no_reply_email}
        )
        mail.attach_alternative(template_body, "text/html")
        mail.send()

    def send_item_create_mail(self, recipient_list, paste_item):
        subject = _(u"Item Created")
        data = highlighter_without_number_helper(paste_item.content, paste_item.syntax.name, css_class="ecxsource")
        context = {
            "subject": subject,
            "data": data,
            "paste_url": "%s%s" % (
                getattr(settings, "BASE_URL"), reverse("item-detail", kwargs={"slug": paste_item.slug})
            )
        }
        template_body = get_template('email/item_create_mail.html').render(Context(context))
        self.send_mail(subject, recipient_list, template_body)
