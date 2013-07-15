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
                    var todo_html = $('#todo-template');

                    $('#todo-list').append('<li><div class="view"><input class="toggle" type="checkbox" value="' + json.id + '" /><label>' + json.title + '</label></div><input type="text" value="' + json.title + '" style="display: none;" /></li>');

                    toggle_footer_links();
                    remove_form_errors();
                    form.resetForm();
                }
            }
        });

        $('.toggle').live('click', function(e) {
            var target = $(e.target);
            target.parents('li:first').toggleClass('completed');
            $.post(complete_todo_url, {'id': target.val()});
        });

        $('#clear-completed').click(function(e) {
            e.preventDefault();
            $.post(clear_completed_url, function(json) {
                var ids = json.ids;
                $.each($('#todo-list :checkbox'), function(index) {
                    if ($.inArray(parseInt($(this).val()), json.ids) !== -1) {
                        $(this).parents('li:first').remove();
                    }
                });
            }, 'json');
        });
    });

    function toggle_footer_links() {
        var todos_length = $('#todo-list li').length;
        if (todos_length > 0) {
            $('#footer div').toggle();
        }
    };
})(jQuery);
