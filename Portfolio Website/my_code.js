// JavaScript source code
// line comments
$(document).ready(function () {
    var imageName = ['/images/logo.png',
        '/images/Drawing (1).png',
        '/images/Drawing (2).png',
        '/images/Drawing (6).png'];
    var imageNum = 0;
    
    $('#logo').click(function () {
        $('#logo').fadeOut(300, function () { 
            $('#logo').attr('src',imageName[imageNum]);
            imageNum++;
            if (imageNum > imageName.length - 1) { imageNum = 0; }
            $('#logo').fadeIn(500);
        });
    });
});

