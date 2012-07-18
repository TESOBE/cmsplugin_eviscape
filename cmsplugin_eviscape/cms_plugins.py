from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import EviscapeInstance
from views import get_sent_evis
from django.utils.translation import ugettext_lazy as _


class EviscapePlugin(CMSPluginBase):
    model = EviscapeInstance
    name = _("Eviscape")
    render_template = "cmsplugin_eviscape/eviscape_plugin.html"

    def render(self, context, instance, placeholder):
        extra_context = {'evis': get_sent_evis(instance.server, instance.nod_id, instance.limit, instance.evis_type),
                         'title': instance.title}
        context.update(extra_context)
        return context

plugin_pool.register_plugin(EviscapePlugin)
