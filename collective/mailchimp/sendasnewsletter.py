from five import grok
from zope.interface import Interface
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from omelette.collective.mailchimp.interfaces import IMailchimpSettings
from omelette.postmonkey import PostMonkey

grok.templatedir("templates")

class SendAsNewsLetterView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')

    def available_lists(self):
        # ask mailchimp which lists are available

        registry = getUtility(IRegistry)
        mailchimp_settings = registry.forInterface(IMailchimpSettings)

        if len(mailchimp_settings.api_key) == 0:
            return []

        coco = PostMonkey(mailchimp_settings.api_key)

        import ipdb; ipdb.set_trace()

        lists = coco.lists()
        listnames = []
#        for lst in lists:
#            name = lst['name']
#            listnames.append(name)

        return listnames