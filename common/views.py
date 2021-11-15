from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import TemplateView


def get_request_context(request, *args, **kwargs):
    context = {'site': get_current_site(request), 'query': request.GET.copy() if request.GET else None}
    return context


def get_common_context(request, *args, **kwargs):
    context = get_request_context(request, *args, **kwargs)
    return context


class BaseView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context.update(get_common_context(self.request, *args, **kwargs))
        return context
