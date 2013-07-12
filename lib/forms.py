from django import forms
from django.template.defaultfilters import striptags


class AjaxBaseForm(forms.BaseForm):
    def errors_as_json(self, strip_tags=False):
        error_summary = {}
        errors = {}
        for error in self.errors.iteritems():
            errors.update({error[0]: unicode(striptags(error[1])
                if strip_tags else error[1])})
        error_summary.update({'errors': errors})
        return error_summary


class AjaxModelForm(AjaxBaseForm, forms.ModelForm):
    """Ajax Form class for ModelForms"""


class AjaxForm(AjaxBaseForm, forms.Form):
    """Ajax Form class for Forms"""
