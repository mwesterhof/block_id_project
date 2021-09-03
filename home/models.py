from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import TestBlock


class HomePage(Page):
    content = StreamField([
        ('test', TestBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]
