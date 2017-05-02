$(document).ready(function () {
    // Button Group: keep the clicked button highlight. 
    $('button').on('click', function () {
        var btnGroupName = $(this).prop('name');
        $('button[name="' + btnGroupName + '"]').removeClass('buttonClicked');
        $(this).addClass('buttonClicked');

        // Update btn-group input hidden value.
        $('input[name="' + btnGroupName + '"]').val($(this).attr('value').trim());
        
        // Set progress bar. 
        var order = $(this).attr('order');
        $('#progress-' + order).removeClass('btn-default-color').addClass('btn-success');
    });

    // FOR Questionnaire 1 (VISA-A) question 8
    var q8_sub_questions = ['#1-9', '#1-10', '#1-11'];

    function display_subquestion(subquestions, qid) {
        // Only display the qid question. 
        subquestions.forEach(function (question) {
            // Clear all checked radio. 
            $(question).find('input[type="radio"]').each(function () {
                $(this).prop("checked", false);
            });
            // Display a sub question. 
            if (question == qid) {
                $(question).show();
                $(question).find('span.question_id').hide();
            }
            else
                $(question).hide();
        });
    }

    // Hide all subquestions when page is loaded. 
    display_subquestion(q8_sub_questions);

    // Set Question 8 events. 
    var options = $("#1-8").find('input[type="radio"]');
    options.on('change', function (ele, idx) {
        var showquestion = options.index(this);
        display_subquestion(q8_sub_questions, q8_sub_questions[showquestion]);
    });

    $('input[type = "radio"]').on('click', function () {
        var radioName = $(this).attr('order');
        if (parseInt(radioName) > 9) {
            radioName = '9';
        }
        $('#progress-' + radioName).removeClass('btn-default-color').addClass('btn-success');
    })
});