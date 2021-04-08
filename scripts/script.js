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