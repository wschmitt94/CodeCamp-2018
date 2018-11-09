var title = document.QuerySelector("H1");
title.style.color("red");
var danger = false;
while(!danger)
	fetch('http://8080/myresource').then(function(response){
		return response.json();
	}).then(function(myResponse){
		console.log(JSON.stringify(myResponse));
	})

if(danger){
	title.style.color("yellow")
}
