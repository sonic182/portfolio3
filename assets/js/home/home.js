'use strict';

export function Home(){

  $(document).ready(function(){
    // Theme javascript
    // Closes the sidebar menu
    $('#menu-close').click(function(e) {
      e.preventDefault();
      $('#sidebar-wrapper').toggleClass('active');
    });

    // Opens the sidebar menu
    $('#menu-toggle').click(function(e) {
      e.preventDefault();
      $('#sidebar-wrapper').toggleClass('active');
    });

    // Scrolls to the selected menu item on the page
    // $();

    (function(){
      $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') || location.hostname === this.hostname) {

          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 1000);
            return false;
          }
        }
      });
    }());

    // wraopper
    (function(){
      // live animation

      // init controller
      var controller = new ScrollMagic.Controller();

      // build scene
      // trigger a velocity opaticy animation
      if ($('.callout').length != 0){
        new ScrollMagic.Scene({triggerElement: '.callout'})
          .setVelocity('#animate', {opacity: 1}, {duration: 900})
          .addTo(controller);
      }

      // .addIndicators() // add indicators (requires plugin)
      // trigger a velocity opaticy animation

      new ScrollMagic.Scene({offset: '100'})
        .setClassToggle('.navbar-default','navbar-dark')
        .addTo(controller);

      if ($('#footer').length != 0){
        new ScrollMagic.Scene({triggerElement: '#footer'})
        // trigger a velocity opaticy animation
          .setClassToggle('.navbar-default','navbar-gone')
          .addTo(controller);
      }

    }());

    // alert('4');
    (function(){
      var controller = new ScrollMagic.Controller;
      $('.service-item .fa-stack').each(function(ind,elem){
        // console.log(ind);
        var val = (ind+1)*900 - (ind+1)*500;
        new ScrollMagic.Scene({
          triggerElement: '#services',
          reverse: false
        })
          .setVelocity(elem, {rotateZ: 360}, {duration: val})
          .addTo(controller);
      });
    }());

    // alert('5');
    (function(){
      // alert('1');
      var controller = new ScrollMagic.Controller;
      // console.log($('#portfolio .section'));
      // alert('asdf');
      // alert('2');
      $('#portfolio .section').each(function(ind,elem){
        // alert('3');
        // var keys = {opacity: '1'};
        // keys[word] = -15;
        // console.log(keys);
        // var val = 900;

        new ScrollMagic.Scene({
          triggerElement: elem,
          reverse: false
        })
          .setVelocity(elem, {opacity: 1}, {duration: 700})
          .addTo(controller);
      });
    }());

  });


  (function(){
    // MAP
    // google.maps.event.addDomListener(window, 'load', init);

    // function init() {
    //   // Basic options for a simple Google Map
    //   // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
    //   var mapOptions = {
    //     // How zoomed in you want the map to start at (always required)
    //     zoom: 15,
    //     scrollwheel: false,
    //
    //     // The latitude and longitude to center the map (always required)
    //     center: new google.maps.LatLng(38.34600, -0.49069), // New York
    //
    //     // How you would like to style the map.
    //     // This is where you would paste any style found on Snazzy Maps.
    //     styles: [	{		'featureType':'landscape',		'stylers':[			{				'hue':'#FFBB00'			},			{				'saturation':43.400000000000006			},			{				'lightness':37.599999999999994			},			{				'gamma':1			}		]	},	{		'featureType':'road.highway',		'stylers':[			{				'hue':'#FFC200'			},			{				'saturation':-61.8			},			{				'lightness':45.599999999999994			},			{				'gamma':1			}		]	},	{		'featureType':'road.arterial',		'stylers':[			{				'hue':'#FF0300'			},			{				'saturation':-100			},			{				'lightness':51.19999999999999			},			{				'gamma':1			}		]	},	{		'featureType':'road.local',		'stylers':[			{				'hue':'#FF0300'			},			{				'saturation':-100			},			{				'lightness':52			},			{				'gamma':1			}		]	},	{		'featureType':'water',		'stylers':[			{				'hue':'#0078FF'			},			{				'saturation':-13.200000000000003			},			{				'lightness':2.4000000000000057			},			{				'gamma':1			}		]	},	{		'featureType':'poi',		'stylers':[			{				'hue':'#00FF6A'			},			{				'saturation':-1.0989010989011234			},			{				'lightness':11.200000000000017			},			{				'gamma':1			}		]	}]
    //   };
    //
    //   // Get the HTML DOM element that will contain your map
    //   // We are using a div with id="map" seen below in the <body>
    //   var mapElement = document.getElementById('map');
    //   // console.log(mapElement);
    //
    //   // Create the Google Map using our element and options defined above
    //   var map = new google.maps.Map(mapElement, mapOptions);
    //
    //   // Let's also add a marker while we're at it
    //   var marker = new google.maps.Marker({
    //     position: new google.maps.LatLng(38.34600, -0.49069),
    //     map: map,
    //     title: 'Snazzy!'
    //   });
    // }
  }());

}
