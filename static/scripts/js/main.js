// Закрытие бокового меню
$('#closeMenu').click(function () {
    $('aside.menu').toggle('slide', {direction: 'left'})
})

// Открытие бокового меню
$('#openMenu').click(function () {
    $('aside.menu').toggle('slide', {direction: 'left'})
})

// Закрытие бокового меню при переходе по якорям
$('a').click(function () {
    if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
        $('aside.menu').toggle('slide', {direction: 'left'})
    }
})

// Закрытие бокового меню при нажатие на другие элементы страницы
$('div.content').click(function () {
    if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
        $('aside.menu').toggle('slide', {direction: 'left'})
    }
})

// Закрытие бокового меню при нажатии esc
$(document).keydown(function (e) {
    // ESCAPE key pressed
    if (e.keyCode === 27) {
        if (document.querySelector('aside.menu').style.display !== 'none' && document.querySelector('aside.menu').style.display !== '') {
            $('aside.menu').toggle('slide', {direction: 'left'})
        }
    }
});