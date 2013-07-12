(function($) {
    $(function() {
        //add csrf token for ajax forms
        $('html').ajaxSend(function(event, xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
        });
    });
})(jQuery);

function remove_form_errors() {
    $('.errorlist').remove();
}

function process_form_errors(json, form) {
    remove_form_errors();

    var prefix = form.data('prefix'),
        errors = json.errors;

    if (errors.__all__ !== undefined) {
        form.append(errors.__all__);
    }

    prefix === undefined ? prefix = '' : prefix += '-';

    for (field in errors) {
        $('#id_' + prefix + field).after(errors[field])
            .parents('.control-group:first').addClass('error');
    }
}
