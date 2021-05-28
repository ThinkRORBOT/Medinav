
window.onload = function () {
    var button = document.getElementById('submit_button');
    button.onclick=function(){

    var u_name = document.getElementById("username").value;
    var pwd = document.getElementById("password").value;
    console.log(u_name);
    if (u_name === "" || pwd === ""){
        window.alert("Please enter a valid username and password");
    } 
    	$.ajax({
	    type: 'POST',
	    url: '/clientnav/',
 	    data: {
 		'u_name': u_name,
		'pwd': pwd
 	    },
 	    success: function(data, textStatus, xhr) {
                console.log(data);
                if (data['status'] == 200) {
                    window.location.href = "/clientnav/selectmix"
                }
                else if (data['status'] == 401) {
                    window.alert("Wrong username password combination");
                }
            },
	});
    return false;
}
};

