/*
function testing(){
  document.getElementById("test").innerHTML = "connected";
  return;
}
*/
var theme = 0;
var themechosen = localStorage.getItem("theme");
if (!typeof(themechosen) == "undefined") {
  theme = themechosen;
  localStorage.setItem("theme",theme);
}
function themechange() {
  theme += 1;
  if (theme > 1) {
    theme = 0;
  };
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
  localStorage.setItem("theme",theme);
};
