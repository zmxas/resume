jQuery(function ($) {

    'use strict';

    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());


    $('.left-col-block, .right-col-block').theiaStickySidebar();

});