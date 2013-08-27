from django.conf import settings
from django.template.base import Library, TemplateSyntaxError, FilterExpression
from django.template.loader import get_template  # import to solve ImportErrors
from django.template.loader_tags import ExtendsNode

register = Library()


class PjaxrExtendsNode(ExtendsNode):
    def __init__(self, nodelist, parent_name, pjaxr_namespace, pjaxr_template, template_dirs=None):
        super(PjaxrExtendsNode, self).__init__(nodelist, parent_name, template_dirs=template_dirs)
        self.pjaxr_namespace = pjaxr_namespace
        self.pjaxr_template = pjaxr_template

    def __repr__(self):
        return '<PjaxrExtendsNode: extends %s>' % self.parent_name.token

    def get_parent(self, context):
        pjaxr_context = dict((k, v) for d in context.dicts for k, v in d.items() if (k == 'pjaxr' or k == 'pjaxr_namespace'))
        if pjaxr_context.get('pjaxr', False):
            try:
                namespace = pjaxr_context['pjaxr_namespace']
            except KeyError:
                self.parent_name = self.pjaxr_template
            else:
                if namespace.startswith(self.pjaxr_namespace.resolve(context)):
                    self.parent_name = self.pjaxr_template

        return super(PjaxrExtendsNode, self).get_parent(context)


@register.tag()
def pjaxr_extends(parser, token):
    bits = token.split_contents()
    if len(bits) != 4 and len(bits) != 3 and len(bits) != 2:
        raise TemplateSyntaxError("'%s' takes 1 - 3 arguments" % bits[0])

    nodelist = parser.parse()

    if nodelist.get_nodes_by_type(PjaxrExtendsNode) or nodelist.get_nodes_by_type(ExtendsNode):
        raise TemplateSyntaxError("'pjaxr_extends' and 'extends' cannot appear more than once in the same template!")

    if len(bits) == 4:
        pjaxr_template = parser.compile_filter(bits[3])
    elif len(bits) == 3:
        try:
            # format DEFAULT_PJAXR_TEMPLATE string to fit into FilterExpression as token
            pjaxr_template = FilterExpression("'{0}'".format(settings.DEFAULT_PJAXR_TEMPLATE), parser)
        except AttributeError:
            raise TemplateSyntaxError("No Pjaxr template set, even no default!")

    if len(bits) > 2:
        return PjaxrExtendsNode(nodelist, parser.compile_filter(bits[1]), parser.compile_filter(bits[2]), pjaxr_template)
    return ExtendsNode(nodelist, parser.compile_filter(bits[1]))
