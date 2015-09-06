from django.conf import settings
from django.contrib.sites.models import Site


def resource_urls(request):
    """Global values to pass to templates"""

    site = Site.objects.get_current()
    defaults = dict(
        STATIC_URL=settings.STATIC_URL,
        SITE_NAME=site.name,
        SITE_DOMAIN=site.domain,
        DEBUG_STATIC=getattr(settings, "DEBUG_STATIC", False),
    )

    return defaults
