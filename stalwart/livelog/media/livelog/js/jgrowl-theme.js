function jGrowlTheme(header, message) {
    var themeAnimate = function() {
        setTimeout( function() {
            $('img.img-thumb').animate({marginLeft: "-.5em"});
            $('.separator').animate({marginLeft: "-.3em"});
            $('div.jGrowl div.themed div.header').animate({marginLeft: "0em"}, 250);
            $('div.jGrowl div.themed div.message').animate({marginLeft: "0em"}, 400);
        }, 10);
    }
    $.jGrowl(message, {
        header: header,
        theme: 'themed',
        life: 10000000,
        open: themeAnimate
    });
}