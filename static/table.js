function fitTextToContainer(
  element,
  maxHeight,
  minFontSize = 10,
  maxFontSize = 30
) {
  let fontSize = maxFontSize;
  element.style.fontSize = fontSize + "px";

  while (element.scrollHeight > maxHeight && fontSize > minFontSize) {
    fontSize -= 1;
    element.style.fontSize = fontSize + "px";
  }
}

var modal = document.getElementsByClassName("book-details");
var card = document.getElementsByClassName("book-card");

card.onclick = function () {
  modal.style.display = "block";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
