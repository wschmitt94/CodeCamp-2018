var title = document.querySelector("h1");
var danger = false;
var isSafe = 'yes';
var childName = 'bobby';

if(danger == false){
	setInterval(checkForDanger, 3000);
	function checkForDanger() {
		
		fetch('http://localhost:8080/myresource').then(function(response){
		return response.json();
	}).then(function(myResponse){
		isSafe = myResponse.status;
		childName = myResponse.name;
	})
}
}


