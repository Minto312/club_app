function showMenu(){
    console.log('showMenu');
    $('.ready-hover').on('mouseenter',(e) => {
        $('.ready-hover').off('mouseenter');
        $(e.currentTarget.children[1]).addClass('showing');
        
        $('.ready-hover').on('mouseleave',(e) => {
            showMenu();
            $('.ready-hover').off('mouseleave');
            $(e.currentTarget.children[1]).removeClass('showing');
                console.log('done');
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    showMenu();
});