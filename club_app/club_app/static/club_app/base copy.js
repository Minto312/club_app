jQuery(function() {
    jQuery(".drop_down_menu_hover").hover(
        function() {
            jQuery(".drop_down_menu_content_hover:not(:animated)", this).slideDown();
        },
        function() {
            jQuery(".drop_down_menu_content_hover", this).slideUp();
        }
    );
});
jQuery(function(){
    jQuery('#user_icon').click(
        function() {
            jQuery(".drop_down_menu_content_click:not(:animated)", this).slideToggle();
        }
    );
    jQuery(document).on('click touchend', function(event) {
        if (!jQuery(event.target).closest('#user_icon:not()').length) {
            jQuery(".drop_down_menu_content_click", this).slideUp();
        }
    });
});