var title = document.querySelector("h1");
var danger = false;

setInterval(checkForDanger, 3000);
function checkForDanger() {

	var d = new Date();
	var time = d.getSeconds();
	if(time % 2){
		danger = true;
	} else {
		danger = false;
	}
	console.log(danger, time);
}


if(danger){
	title.style.color = "yellow";
} else {
	title.style.color = "red";
}
