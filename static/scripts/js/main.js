$('#closeMenu').click(function () {
    $('aside.menu').toggle('slide', {direction: 'left'})
})
$('#openMenu').click(function () {
    $('aside.menu').toggle('slide', {direction: 'left'})
})
$('a').click(function () {
    if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
        $('aside.menu').toggle('slide', {direction: 'left'})
    }
})

$('div.content').click(function () {
    if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
        $('aside.menu').toggle('slide', {direction: 'left'})
    }
})

$(document).keydown(function (e) {
    // ESCAPE key pressed
    if (e.keyCode === 27) {
        if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
            $('aside.menu').toggle('slide', {direction: 'left'})
        }
    }
});