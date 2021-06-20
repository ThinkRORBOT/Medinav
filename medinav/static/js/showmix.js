
window.onload = function () {
    var button = document.getElementById('select_button');
    button.onclick=function(){
        
    	$.ajax({
	    type: 'POST',
	    url: '/clientnav/showmix/',
 	    data: {
 		'action': 1,
 	    },
 	    success: function(data, textStatus, xhr) {
                console.log(data);
                if (data['status'] == 200) {
                    console.log('db updated')
                }
                else if (data['status'] == 401) {
                    window.alert("Something went wrong");
                }
            },
	});
    return false;
    }
    var reset_button = document.getElementById('reset_button');
    reset_button.onclick=function(){
        
    	$.ajax({
	    type: 'POST',
	    url: '/clientnav/showmix/',
 	    data: {
 		'action': 0,
 	    },
 	    success: function(data, textStatus, xhr) {
                console.log(data);
                if (data['status'] == 200) {
                    console.log('db updated')
                }
                else if (data['status'] == 401) {
                    window.alert("Something went wrong");
                }
            },
	});
    return false;
}
};
 
