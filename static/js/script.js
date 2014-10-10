$(document).ready(function(){
	    $('#clickme').click(function(){
	 $.ajaxSetup({
	     success: function(data){
	  data = $.parseJSON(data);
	                alert(data['new-text']);
	            }
	         });
	       $.post('/ajax/test/', {'text': $('#test-ajax').val()});
	});
