if (!('stoa' in window)) {
    window.stoa = {
    }
}
jQuery(function (a) {
    window.stoa.click_event = a.fn.tap ? 'tap' : 'click'
});
jQuery(function (a) {
    stoa.handle_side_menu(jQuery)
});
stoa.handle_side_menu = function (a) {
    a('#menu-toggler') .on(stoa.click_event, function () {
        a('#sidebar') .toggleClass('display');
        a(this) .toggleClass('display');
        return false
    });
    var c = a('#sidebar') .hasClass('menu-min');
    a('#sidebar-collapse') .on(stoa.click_event, function () {
        c = a('#sidebar') .hasClass('menu-min');
        stoa.settings.sidebar_collapsed(!c);
        if (c) {
            //Collapse Sidebar
            M.util.set_user_preference('stoa_sidebar', 1);
        } else {
            //Fixed Sidebar
            M.util.set_user_preference('stoa_sidebar', 0);
        }
        
    });
    var b = navigator.userAgent.match(/OS (5|6|7)(_\d)+ like Mac OS X/i);
    a('.nav-list') .on(stoa.click_event, function (h) {
        var g = a(h.target) .closest('a');
        if (!g || g.length == 0) {
            return
        }
        c = a('#sidebar') .hasClass('menu-min');
        if (!g.hasClass('dropdown-toggle')) {
            if (c && stoa.click_event == 'tap' && g.get(0) .parentNode.parentNode == this) {
                var i = g.find('.menu-text') .get(0);
                if (h.target != i && !a.contains(i, h.target)) {
                    return false
                }
            }
            if (b) {
                document.location = g.attr('href');
                return false
            }
            return
        }
        var f = g.next() .get(0);
        if (!a(f) .is(':visible')) {
            var d = a(f.parentNode) .closest('ul');
            if (c && d.hasClass('nav-list')) {
                return
            }
            d.find('> .open > .submenu') .each(function () {
                if (this != f && !a(this.parentNode) .hasClass('active')) {
                    a(this) .slideUp(200) .parent() .removeClass('open');
                }
            })
            // Visible Block
            M.util.set_user_preference('stoa_block', a(f.parentNode).prop('id'));
            
            //Turn hidden other blocks
            a(f).parent().parent().find('.open > .submenu').slideToggle(200);
            a(f).parent().parent().find('.open.active').removeClass('open').removeClass('active');

            //Open specific block (onclick)
            a(f) .slideToggle(200) .parent() .toggleClass('open');
            a(f) .parent() .toggleClass('active'); 

        } else {
            //Turn hidden other blocks
            a(f).parent().parent().find('.open > .submenu').slideToggle(200);
            a(f).parent().parent().find('.open.active').removeClass('open').removeClass('active');

            // Hidden Block
            M.util.set_user_preference('stoa_block', 0);
        }
        if (c && a(f.parentNode.parentNode) .hasClass('nav-list')) {
            return false
        }

        return false
    })
};


/*
autor: Marisa Endruveit 2014 (adaptação de http://www.bootply.com/tagged/sidebar)
*/
