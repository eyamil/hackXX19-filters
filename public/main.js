var imageTag = document.getElementsByTagName("img")[0];
var fileSelector = document.getElementsByTagName("input")[0];
fileSelector.onchange = function(event) {

    var target = event.target || window.event.srcElement;
    var files = target.files;

    if (FileReader && files && files.length) {
    
        var reader = new FileReader(files);
        reader.onload = function() {
        
            imageTag.src = reader.result;
        
        }
        reader.readAsDataURL(files[0]);

    }

}
