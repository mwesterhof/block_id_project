# from uuid import uuid4

from uuid import uuid4

from django import forms
from wagtail.core import blocks
from wagtail.core.telepath import register


class IDBlock(blocks.CharBlock):
    def clean(self, value):
        result = super().clean(value)
        if not result:
            result = str(uuid4())
        return result


class IDBlockAdapter(blocks.field_block.FieldBlockAdapter):
    def js_args(self, block):
        result = super().js_args(block)
        result[1] = forms.widgets.TextInput(attrs={'readonly': 'readonly'})
        # result[1] = forms.widgets.HiddenInput()
        return result


register(IDBlockAdapter(), IDBlock)


class TestBlock(blocks.StructBlock):
    block_id = IDBlock(required=False, label='--')
    name = blocks.CharBlock()

    class Meta:
        template = 'home/blocks/test.html'
