
  (function ($) {
  
  "use strict";

    // COUNTER NUMBERS
    jQuery('.counter-thumb').appear(function() {
      jQuery('.counter-number').countTo();
    });
    
    // CUSTOM LINK
    $('.smoothscroll').click(function(){
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped,header_height);
    return false;

    function scrollToDiv(element,navheight){
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop-navheight;

      $('body,html').animate({
      scrollTop: totalScroll
      }, 300);
    }
});
    
  })(window.jQuery);

  function eliminarUsu(id) {
    Swal.fire({
        icon: 'warning',
        title: 'Estás seguro?',
        text: 'No podrás deshacer la acción!',
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: '#3085d6',
        cancelButtonText: "Cancelar"
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Eliminado!',
            'Usuario eliminado Correctamente',
            'success'
          ).then(function() {
            window.location.href = "/eliminar_usuario/"+ id +"/"
          })
        }
      })
  }
