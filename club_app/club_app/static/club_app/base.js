function isSmartPhone() {
    // UserAgentからのスマホ判定
    if (navigator.userAgent.match(/iPhone|iPod|iPad|Android/)) {
      return true;
    } else {
      return false;
    }
  }
  

function showMenu(){
    console.log('showMenu');
    if(isSmartPhone() || true){
        $('.ready-hover').on('click',(e) => {
            if ($(e.currentTarget.children[1]).hasClass('showing')){
                $(e.currentTarget.children[1]).removeClass('showing');
            }else{
                $('.showing').removeClass('showing');
                $(e.currentTarget.children[1]).addClass('showing');
                $('#content').on('click',(e) => {
                    $('.showing').removeClass('showing');
                    $('body').off('click');
                });
            }
        });
    }else{
        // $('.ready-hover').on('mouseenter',(e) => {
        //     $('.ready-hover').off('mouseenter');
        //     $(e.currentTarget.children[1]).addClass('showing');
            
        //     $('.ready-hover').on('mouseleave',(e) => {
        //         showMenu();
        //         $('.ready-hover').off('mouseleave');
        //         $(e.currentTarget.children[1]).removeClass('showing');
        //             console.log('done');
        //     });
        // });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    showMenu();
});