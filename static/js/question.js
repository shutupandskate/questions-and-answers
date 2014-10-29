$(document).ready(function(){

    var bookmarkButton = $("#bm-button");
    var addAnswerForm = $(".add-answer");
    var sendAnswerButton = $("#sendAnswer");
    var upButtons = $(".vote-up");
    var downButtons = $(".vote-down");

    var qvotes = $('#qvotes_num').attr('qvotes'); 
    var ans_num = $('#answer_list').attr('ans_num');

    bookmarkButton.on("click", function(){
        bm(this);
    });

    upButtons.on("click", function(){
        //console.log(this);
        vote(this, "up");
    });

    downButtons.on("click", function(){
        vote(this, "down");
    });

    sendAnswerButton.on("click", function(e){
        e.preventDefault();
        if($('#id_content').val()) {
            addAnswer(this);
        }
    });


    function bm(_this) {
        var button = $(_this);
        var bm_count = $(".bm-button__count").find("span");

        $.ajax(
        {
            data: {
                'q_id' : button.attr('q_id'), // question id
                //'bm_num' : button.attr('bm_num') // count of bm's
            },
            type: 'POST',
            url: 'bm/',
            success: function(data, status) {
                if (button.hasClass("marked")) { // if it was pressed
                    button.removeClass("marked").removeClass("btn-inverse");
                    button.find("i").removeClass("icon-white").addClass("icon-black");
                    button.find("span").text("bookmark");
                    bm_count.text(parseInt(bm_count.text()) - 1);
                } else { // if it was not pressed
                    button.addClass("marked").addClass("btn-inverse");
                    button.find("i").removeClass("icon-black").addClass("icon-white");
                    button.find("span").text("bookmarked");
                    bm_count.text(parseInt(bm_count.text()) + 1);
                }
            },
            error: function(xhr, data) {
                alert('Please, log in for this operation');
            }
        });
    }


    function vote(_this, action) {
        var button = $(_this);
        var type = button.parent().attr("type"); // answer or question
        var id = button.parent().attr("id"); // id of answer or question

        console.log(button, type, id);

        var votesNumberBlock = $(button.parent().find(".votes-number"));
        var upButton = $(button.parent().find(".vote-up"));
        var downButton = $(button.parent().find(".vote-down"));

        var url = "/" + type + "/" + id + "/vote/";
        url = (action == "up") ? url + "up/" : url + "down/";
        var pressed = "vote-button_pressed";
        var diff = 0;

        $.ajax(
        {
            data: {
                'id' : id
            },
            type: 'POST',
            url: url,
            success: function(data, status) {
                if(action == 'up') {
                    if(upButton.hasClass(pressed)) {
                        upButton.removeClass(pressed);
                        diff = -1;
                        console.log("1");
                    } else if(downButton.hasClass(pressed)){
                        downButton.removeClass(pressed);
                        upButton.addClass(pressed);
                        diff = 2;
                        console.log("2");
                    } else {
                        upButton.addClass(pressed);
                        diff = 1;
                        console.log("3");
                    }
                } else if(action == 'down') {
                    if(downButton.hasClass(pressed)) {
                        downButton.removeClass(pressed);
                        diff = 1;
                        console.log("4");
                    } else if(upButton.hasClass(pressed)) {
                        upButton.removeClass(pressed);
                        downButton.addClass(pressed);
                        diff = -2;
                        console.log("5");
                    } else {
                        downButton.addClass(pressed);
                        diff = -1;
                        console.log("6");
                    }
                }
                votesNumberBlock.text(parseInt(votesNumberBlock.text()) + diff);
            },
            error: function(xhr, data) {
                //alert('Please, log in for this operation');
            }
        });
    }

    function addAnswer(_this){
        var form = $(_this).parent();
        var content = form.find('#id_content').val();
        var q = form.find('.q_id').val();
        var author = form.find('.author').val();

        $.ajax({
            data: {
                'content': content,
                'q': q,
                'author': author
            },
            type: 'POST',
            url: 'a/',
            success: function(data, status) {
                $("#noanswer").hide();
                $("#ans_num").text(parseInt($("#ans_num").text()) + 1);

                var answer =
                    "<div class='answer-list__item'>" +
                        "<div class='user-block user-block_answer thumbnail'>" +
                            "<div class='text-block'>" +
                                "<div class='text-block__item'>" +
                                    "author <b>you</b>" +
                                "</div>" +
                                "<div class='text-block__item'>" +
                                    "answered <b>now</b>" +
                                "</div>" +
                            "</div>" +
                        "</div>" +
                        "<p>" + content + "</p>" +
                        "<div class='clearfix'></div>" +
                    "</div>";
                $("#answer-list").append(answer);
                $("#id_content").val('');
            }
        });
    }


});
