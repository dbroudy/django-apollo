function submitQuestionForm() {
  var $f = $('#questionsForm');
  $('.saving', $f).html('Saving...');
  $.ajax({
    url: $f.attr('action'),
    type: 'POST',
    data: $f.serializeArray(),
    complete: function(xhr) {
      if (xhr.status == 202) {
        $('.saving', $f).html('Survey saved.');
      } else if (xhr.status == 200) {
        $f.fadeOut(1200);
      }
    }
  });
}

$(function() {
  $('.btn-register').click(function() {
    $.ajax({
      url: $(this).attr('href'),
      success: function(partial) {
        var timeout;
        $('#buttons_wrapper').replaceWith(partial);
        $('#questionsForm input').change(function() {
          clearTimeout(timeout);
          timeout = setTimeout(submitQuestionForm, 1000);
        });
      }
    });
  });
});
