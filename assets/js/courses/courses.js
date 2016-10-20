export function Courses () {
  var controller = new ScrollMagic.Controller();

  // new ScrollMagic.Scene({triggerElement: '#footer'})
  // .setClassToggle('.navbar-default','navbar-gone')
  // .addTo(controller);

  var elem = $('.subscription_form');
  var elem2 = $('.course_info');
  var $window = $(window)

  if (elem.length != 0){
    $(window).scroll(() => {
      // console.log(elem.position())
      // console.log()
      // console.log(elem.css('position'))
      var elemTop = elem2.offset().top
      var windowTop = $window.scrollTop()
      // console.log(`${elemTop} <= ${windowTop}`)
      if ( elemTop <= windowTop ){
        // console.log(elem.parent().width())
        if (elem.css('position') != 'fixed'){
          if ($window.width() > 768){
            elem.css({
              width: elem.parent().width().toString(),
              position: 'fixed',
              top: '15px'
            })
          }
        }
      }else{
        if (elem.css('position') != 'relative'){
          elem.css({
            width: '100%',
            position: 'relative',
            top: 'auto'
          })
        }
      }
    })
  }

}
