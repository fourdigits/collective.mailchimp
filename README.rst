Introduction
============

MailChimp (http://mailchimp.com) integration for Plone.

MailChimp helps you design email newsletters, share them on social networks,
integrate with services you already use, and track your results.

Right now this is an experimental package only. If you are looking for a
MailChimp integration for Plone have a look at raptus.mailchimp (http://plone.org/products/raptus.mailchimp).

The difference between raptus.mailchimp and collective.mailchimp is:

- PostMonkey instead of greatape as Python wrapper.
- z3c.form instead of formlib for forms.
- plone.app.registry instead of portal_properties for storing properties.

collective.mailchimp is tested on Plone 4.x and should work on Plone > 3.3
(with the appropriate version pins).
