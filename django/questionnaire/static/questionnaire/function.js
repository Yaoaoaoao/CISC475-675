$(document).ready(function () {
    function afterClick(index) {
        for (var i = 0; i < buttons.length; i++) {
            if (i == index) {
                buttons[i].id = "buttonAfterClick";
                var question_id = buttons[i].getAttribute("name");
            }
        }
        for (var i = 0; i < buttons.length; i++) {
            if (i !== index && buttons[i].name == question_id) {
                buttons[i].removeAttribute("id");
            }
        }
    }

    var buttons = $("button");
    for (var i = 0; i < buttons.length; i++) {
        var j = i;
        buttons[j].addEventListener("click", function () {
            afterClick(j);
        }, false);
    }


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
    $("#1-8").find('input[type="radio"]').on('change', function () {
        var option = $(this).val();
        var showquestion = parseInt(option) - 1;
        display_subquestion(q8_sub_questions, q8_sub_questions[showquestion]);
    })
});