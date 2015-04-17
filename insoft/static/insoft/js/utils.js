
function showGalary() {
    console.log(arguments);
    var pswpElement = document.querySelectorAll('.pswp')[0],
        title = arguments[0],
        items = [];
    for (var i = 1; i < arguments.length; ++i)
        items.push({src:'/media/' + arguments[i],
            title: title,
            w: 1000,
             h: 1334
        });
    /*
    var items = [{
            src:
        },
        {
            src: 'https://placekitten.com/1200/900'
//            w: 1200,
 //           h: 900
        }
    ];
    */

// define options (if needed)
    var options = {
        index: 0, // start at first slide
        bgOpacity: 0.3,
        shareEl: false
    };

// Initializes and opens PhotoSwipe
    var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
    gallery.init();
}
