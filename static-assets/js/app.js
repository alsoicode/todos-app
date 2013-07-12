(function($) {
    $(function() {
        // handle submitting the form via Ajax using the jQuery
        // form plugin

        $('#new-todo-form').ajaxForm({
            dataType: 'json',
            url: this.action,
            beforeSubmit: function(arr, form, options) {
                form.find('.activity').show();
            },
            success: function(json, status, xhr, form)
            {
                form.find('.activity').hide();

                if (json.errors !== undefined) {
                    process_form_errors(json, form);
                }
                else {
                    remove_form_errors();
                    form.resetForm();
                }
            }
        });
    });
})(jQuery);
