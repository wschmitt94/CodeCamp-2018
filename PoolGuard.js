var child_1_button = document.querySelector("#check");
var children = document.querySelector(".children");
var warning = document.querySelector("#warning");
var dismiss = document.querySelector("#dismiss");

var danger = false;
var num_children = 1;
var status = 'yes';
var child_name = 'bobby';

function checkForDangerAll() {
	fetch('http://localhost:8080/children').then(function(response){
		return response.json();
	}).then(function(myResponse){
		for (var i = myResponse.length - 1; i >= 0; i--) {
			CheckForDangerOne(myResponse[i]);
		}
	})
}

function CheckForDangerOne(child) {
	fetch('http://localhost:8080/children/' + child).then(function(response){
		return response.json();
	}).then(function(myResponse){
		status = myResponse.status;
		child_name = myResponse.name;
		if(status == "danger"){
			child_name = child_name.toUpperCase();
			danger = true;
			var text = warning.querySelector('h2');
			text.innerHTML = child_name + " IS IN IMMINENT PERIL";
			warning.style.display = "block";
		}
	})
}

child_1_button.onclick = function() {
	var child1 = children.querySelector("h3");
	var child_name = child1.innerHTML;
	CheckForDangerOne(child_name);
	if(danger == false){
		alert(child_name + " is safe");
	}
}

dismiss.onclick = function() {
	warning.style.display = "none";
	danger = false;
}

if(danger == false){
	setInterval(checkForDangerAll, 3000);
}