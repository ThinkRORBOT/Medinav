
window.onload = function () {
    var button = document.getElementById('select_button');
    button.onclick=function(){

    var drug_prop = document.getElementById("selectdrug").value;
    console.log(drug_prop);
    if (drug_prop === ""){
        window.alert("Please select a drug first");
    }
        var split_string = drug_prop.split("|");
        var drug_id = drug_prop[0];
        
    	$.ajax({
	    type: 'POST',
	    url: '/clientnav/selectmix/',
 	    data: {
 		'drug_id': drug_id,
 	    },
 	    success: function(data, textStatus, xhr) {
                console.log(data);
                if (data['status'] == 200) {
                    window.location.href = "/clientnav/showmix"
                }
                else if (data['status'] == 401) {
                    window.alert("Something went wrong");
                }
            },
	});
    return false;
}
};
