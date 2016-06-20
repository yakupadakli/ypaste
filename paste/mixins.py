import datetime

from paste.models import PasteItem


class SessionMixin(object):
    session_id = None

    def set_cookie(self, response, key, value, days_expire=365):
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(days=days_expire), "%a, %d-%b-%Y %H:%M:%S GMT"
        )
        response.set_cookie(key, value, expires=expires)

    def get(self, request, *args, **kwargs):
        if self.request.COOKIES.get("sessionid"):
            self.session_id = self.request.COOKIES.get("sessionid")
        else:
            self.session_id = PasteItem.create_unique_session_id()
        response = super(SessionMixin, self).get(request, *args, **kwargs)
        self.set_cookie(response, 'sessionid', self.session_id)
        return response

    def get_form_kwargs(self):
        kwargs = super(SessionMixin, self).get_form_kwargs()
        kwargs["session"] = self.session_id
        return kwargs
