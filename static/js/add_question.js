console.log($("#add-question__submit"));
$("#add-question__submit").on("click", function(e){
    e.preventDefault();
    var form = $(this).parent();
    if (validate(form)) {
        form.submit();
    } else {
        $(".validity-error").show();
    }
});

function validate(form) {
    if((form.find("#id_head").val() == '') || (form.find("#id_content").val() == ''
        || (form.find("#id_tags").val() == ''))) {
        return false;
    } else {
        return true;
    }
}

