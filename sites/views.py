from django.views import generic
from django.db.models import Sum

from .models import Site


class ExtraContext:
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class SiteListView(ExtraContext, generic.ListView):
    model = Site


class SiteDetailView(ExtraContext, generic.DetailView):
    model = Site


class SiteSummaryView(ExtraContext, generic.ListView):
    model = Site
    template_name = 'sites/site_summary.html'

    queryset = Site.objects.annotate(a_value=Sum('details__a_value'), b_value=Sum('details__b_value'))


class SiteSummaryAverageView(SiteSummaryView):
    model = Site

    queryset = Site.objects.raw('SELECT sites.id, title, round(avg(CAST(a_value AS FLOAT)), 2) AS a_value, round(avg(CAST(b_value AS FLOAT)), 2) AS b_value\
        FROM sites_site as sites LEFT OUTER JOIN sites_siteinfo as site_infos on sites.id = site_infos.site_id\
        GROUP BY site_infos.site_id order by sites.id')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['child'] = True
        return context
