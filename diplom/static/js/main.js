// Голый Java Script
down.onclick = function () {
    let el = document.querySelector('#showmenu');   
    el.style.maxHeight = '350px';
    document.querySelector('.fa-angles-down').style.display = 'none';
    document.querySelector('.fa-angles-up').style.display = 'block';
    }

up.onclick = function () {
    let el = document.querySelector('#showmenu');   
    el.style.maxHeight = '0px';
    document.querySelector('.fa-angles-down').style.display = 'block';
    document.querySelector('.fa-angles-up').style.display = 'none';
    }    

// Немного JQuery
// Копирование в буфер обмены ссылки
$('#links div p').on("click", function() {
    let url = $(this).children('a').attr('href')
    navigator.clipboard.writeText(document.location.href + '' + url)
})

// Удаление информационных сообщений через 3 секунды
$(document).ready(function(){
    $('.messages li.error').fadeOut(3000);
    $('.messages li.success').fadeOut(3000);
});

// Запрос на удаление ссылки. Сделан через GET. Неправильно конечно, но пока пусть так.
function confirm_delete(id){
    if (confirm("Вы уверены, что хотите удалить ссылку?")) {
        window.location.href=(document.location.href + '' + "del_link/" + id)
    }
}

// РАбота с картинками
$(function(){
    $("a.colorbox").colorbox();
});

$("a.colorbox").colorbox({
    maxWidth:"100%",
    maxHeight:"100%",
    opacity:"0.8",
});