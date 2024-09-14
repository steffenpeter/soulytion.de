let isVisible = false;
jQuery(document).ready(function(){
	// Mobile
	jQuery('.mobilemenu_toggle').click(function(eventObject) {
		eventObject.preventDefault();
   isVisible = !isVisible;
   if (isVisible) {
		jQuery(this).parents('.menuwrapp_mobile').find('.menu_mobile').slideDown(200);
   } else {
		jQuery(this).parents('.menuwrapp_mobile').find('.menu_mobile').slideUp(200);
   }

	});	

}); //Final ready
