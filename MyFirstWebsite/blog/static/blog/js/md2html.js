var converter = new showdown.Converter({parseImgDimensions: true})
var elements = document.getElementsByClassName("md2html");
for(var i = 0; i < elements.length; i++){
   //do something to each div like
   var text = elements[i].innerHTML;
   elements[i].innerHTML = converter.makeHtml(text);
}