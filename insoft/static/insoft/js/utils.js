/**
 * Показывает рисунки поверх сайта (галерея)
 * @param {String} title - подпись для рисyнков
 * @param {Object[]} scans - рисунки
 */
function showGalary(title, scans) {
    var pswpElement = document.querySelectorAll('.pswp')[0],
        title = arguments[0],
        items = [];
    scans.forEach(function(it){
      items.push({src: '/media/' + it.src,
          title: title, w: it.w, h: it.h});
    });

    var options = {
        index: 0, // start at first slide
        bgOpacity: 0.5,
        shareEl: false
    };

    var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
    gallery.init();
}
