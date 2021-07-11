logos = document.getElementsByClassName("logo")
texts = document.getElementsByClassName("text")
texts20 = document.getElementsByClassName("text20")
texts20mid = document.getElementsByClassName("text20mid")
directs = document.getElementsByClassName("direct")
if (screen.width >= 600) {
	for (var i = 0; i < logos.length; i++) {
   		logos[i].style.width = "600px";
	}
}
else {
	for (var i = 0; i < logos.length; i++) {
   		logos[i].style.width = "100%";
	}
	for (var i = 0; i < texts.length; i++) {
   		texts[i].style.margin = "30px 10%";
	}
	for (var i = 0; i < texts20.length; i++) {
   		texts20[i].style.margin = "30px 5%";
	}
	for (var i = 0; i < texts20mid.length; i++) {
   		texts20mid[i].style.margin = "30px 5%";
	}
	for (var i = 0; i < texts20mid.length; i++) {
   		texts20mid[i].style.margin = "30px 5%";
	}
	for (var i = 0; i < directs.length; i++) {
   		directs[i].style.height = "35px";
		directs[i].style.width = "100%";
		directs[i].style.border = "3px solid #ffaa00"
	}
}

function switchth() {
	switch (theme) {
    case 0:
    document.body.style.backgroundColor = "white";
    document.body.style.color = "black";
    break;
    case 1:
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
    break;
  };
};

function themechange() {
	theme += 1;
	if (theme > 1) {
		theme = 0;
	};
	switchth();
	localStorage.setItem("theme",theme);
};

var theme = 0;
var themechosen = parseInt(localStorage.getItem("theme"));
theme = themechosen;
if (!typeof(themechosen) == "undefined") {
	theme = themechosen;
	localStorage.setItem("theme",theme);
};
switchth();