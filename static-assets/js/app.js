(function($) {
    $(function() {
        // handle submitting the form via Ajax using the jQuery form plugin
        var new_todo_form = $('#new-todo-form'),
            activity_indicator = new_todo_form.find('.activity');

        new_todo_form.ajaxForm({
            dataType: 'json',
            url: this.action,
            beforeSubmit: function(arr, form, options) {
                activity_indicator.show();
            },
            success: function(json, status, xhr, form)
            {
                activity_indicator.hide();

                if (json.errors !== undefined) {
                    process_form_errors(json, form);
                }
                else {
                    $('#todo-list').append('<li><div class="view"><input class="toggle" type="checkbox" value="' + json.id + '" /><label>' + json.title + '</label></div><input type="text" value="' + json.title + '" style="display: none;" /></li>');
                    toggle_clear_select_all();
                    remove_form_errors();
                    form.resetForm();
                    set_todo_count();
                }
            }
        });

        // toggle if todo is complete
        $('.toggle').live('click', function(e) {
            var target = $(e.target);
            target.parents('li:first').toggleClass('completed');
            $.post(complete_todo_url, {'id': target.val()});
        });

        // delete any completed toods
        $('#clear-completed').click(function(e) {
            e.preventDefault();
            $.post(clear_completed_url, function(json) {
                var ids = json.ids;
                $.each($('#todo-list :checkbox'), function(index) {
                    if ($.inArray(parseInt($(this).val()), json.ids) !== -1) {
                        $(this).parents('li:first').remove();
                    }
                });
            }, 'json').done(function() {
                toggle_clear_select_all();
                set_todo_count();
            });
        });

        // toggle all of the todos
        $('#toggle-all').click(function(e) {
            $('.toggle').trigger('click');
        });

        // Show All todos
        $('#filter-all').click(function(e) {
            $('#todo-list li').show();
        });

        // Filter active todos
        $('#filter-active').click(function(e) {
            $('#todo-list').find('.completed').hide().end().find('li[class!="completed"]').show();
        });

        // Filter completed todos
        $('#filter-completed').click(function(e) {
            $('#todo-list').find('.completed').show().end().find('li[class!="completed"]').hide();
        });
    });

    function count_todos() {
        return $('#todo-list li').length;
    }

    function set_todo_count() {
        var todo_count = count_todos(),
            items = $('#count-info .items'),
            items_text = '';

        $('#count-info .number').text(todo_count);

        if (todo_count === 0 || todo_count > 1) {
            items_text = 'items';
        }
        else {
            items_text = 'item';
        }
        items.text(items_text);
    }

    // show/hide any elements that are related to the count of todos
    function toggle_clear_select_all() {
        var clear_completed = $('#footer div'),
            toggle_all_todos = $('#toggle-all');

        if (count_todos() > 0) {
            clear_completed.show();
            toggle_all_todos.show();
        }
        else {
            clear_completed.hide();
            toggle_all_todos.hide();
        }
    }
})(jQuery);
