from z3c.form import form
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from collective.mailchimp.interfaces import IMailchimpSettings
from postmonkey import PostMonkey
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

class SendAsNewsLetterView(BrowserView):
    template = ViewPageTemplateFile('sendasnewsletter.pt')


    def __call__(self):

        # check of het een POST is, dan code ter signup runnen
        if 'submitbutton' in self.request.form.keys():
            # find all 'list_xxx' keys. These are the ids of the lists we want to sign up for
            if 'emailaddress' in self.request.form.keys():
                emailaddress = self.request.form['emailaddress']
                #check for validity?

                ids = [l_id[5:] for l_id in self.request.form.keys() if 'list_' in l_id]
                if len(ids) > 0:
                    registry = getUtility(IRegistry)
                    mailchimp_settings = registry.forInterface(IMailchimpSettings)
                    if len(mailchimp_settings.api_key) == 0:
                        return []

                    # we have an api key, and at least a list to subscribe to
                    print 'Sign up for: ' + str(ids)

                    coco = PostMonkey(mailchimp_settings.api_key)
                    mergevars = {'FNAME': ''}
                    for list_id in ids:
                        coco.listSubscribe(
                            id=list_id,
                            email_address=emailaddress,
                            merge_vars=mergevars,
                        )
                        print 'Signed ' + emailaddress + ' up for list ' + list_id

        return self.template()
            # redirect naar x

    def current_email_address(self):

        membership_tool = getToolByName(self.context, 'portal_membership')
        import ipdb; ipdb.set_trace()
        member = membership_tool.getAuthenticatedMember()
        if member:
            return member.
        else:
            return None

    def available_lists(self):
        # ask mailchimp which lists are available
        # maybe also ask system which lists we are allowed to send to

        # these lists have an id
        registry = getUtility(IRegistry)
        mailchimp_settings = registry.forInterface(IMailchimpSettings)

        if len(mailchimp_settings.api_key) == 0:
            return []

        coco = PostMonkey(mailchimp_settings.api_key)

        lists = coco.lists()['data']
        list_infos = []
        for lst in lists:
            list_id = 'list_' + lst['id']
            name = lst['name']
            list_info = {
                'id': list_id,
                'name': name
            }
            list_infos.append(list_info)

        return list_infos