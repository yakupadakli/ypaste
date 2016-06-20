class PasteMiddleware(object):

    def process_request(self, request):
        request.is_json = False
        if request.GET.get("format") == "json":
            request.is_json = True
        return None
