
$('#copyright').text(new Date().getFullYear());

$(window).on('resize', function(){
    const win = $(this);
    if (win.width() >= 707) { 
        $("div.navbar-links-list-div").css('top', '4px')
     }
    if (win.width() <= 707) { 
        $("div.navbar-links-list-div").css('top', '-192px')
    }
});

$('div.menu-icon').on('click', function () {
    if ($("div.navbar-links-list-div").css('top') === '-192px') {
        $("div.navbar-links-list-div").css('top', '64px')
    }
    else if ($("div.navbar-links-list-div").css('top') === '64px') {
        $("div.navbar-links-list-div").css('top', '-192px')
    }
})