/********************************************************/
/*                                                      */
/*  jquery.CarouselLifeExample.js                       */
/* Плагин "Карусель от LifeExample.ru" для jQuery        */
/*  Автор: Авдеев Марк                                   */
/*              2012г.                                 */
/*                                                      */
/* Для ипользования плагина необходимо определить     */
/* контейнер и вложить в него маркерованный список:        */
/*                                                      */
/*  <div class="container">                             */
/*                <ul class="carousel">                 */
/*                        <li>1</li>                    */
/*                        <li>2</li>                    */
/*                        <li>3</li>                    */
/*                        <li>4</li>                    */
/*                        <li>5</li>                    */
/*                        <li>6</li>                    */
/*                </ul>                                 */
/*    </div>                                            */
/* После чего можно указать параметры для использования */
/* плагина                                               */
/* $('.container').Carousel({                           */
/*  visible: 3,  //количество отображаемых позиций 3   */
/*  rotateBy: 1, //прокручивать по 1                  */
/*  speed: 1000, //скорость 1 секунда                    */
/*  btnNext: null, // кнопка вперед не назначена     */
/*  btnPrev: null, // кнопка назад не назначена           */
/*  auto: true, // авто прокрутка включена             */
/*  margin: 10, // отступ между позициями               */
/*  dirAutoSlide: false //направление движения           */
/*  });                                                 */
/*  Или использовать параметры по умолчанию              */
/*  $('.container').Carousel();                         */
/*                                                      */
/*******************************************************/
(function ($) {
    $.fn.Carousel = function (options) {
        // Настройки по умолчанию
        var settings = {
            visible: 3,  //количество отображаемых позиций 3
            rotateBy: 1, //прокручивать по 1
            speed: 1000, //скорость 1 секунда
            btnNext: null, // кнопка вперед не назначена
            btnPrev: null, // кнопка назад не назначена
            auto: true, // авто прокрутка включена
            margin: 0,    // отступ между позициями
            dirAutoSlide: false //направление движения вперед для автопрокрутки
        };

        return this.each(function () {
            if (options) {
                $.extend(settings, options); //устанавливаем пользовательские настройки
            }

            // определяем переменные
            var $this = $(this),//родительский элемент (Блок в котором находится карусель)
                $carousel = $this.children(':first'),// получаем дочерний элемент (UL) т.е. саму карусель
                itemsTotal = $carousel.children().length, // получаем общее количество элементов в каруселе
                running = false, //останавливаем процесс
                intID = null,
                elIcrease = 2 * settings.margin; //отчищаем интервал

            function getVisibleWidth() {
                 var visibleWidth = 0;
                $carousel.children().each(function (i, it) {
                    if (i < settings.visible) {
                        visibleWidth += $(it).outerWidth();
                    } else {
                        return false;
                    }
                });
                return (visibleWidth + settings.visible * elIcrease) + 'px';
            }

            function getSumWidth(items) {
                var width = 0;
                items.each(function(_, it){
                    width += $(it).outerWidth();
                });
                return width + items.length * elIcrease;
            }

            $carousel.children('li').css({
                'margin-left': settings.margin + 'px',
                'margin-right': settings.margin + 'px'
            });

            $this.css({
                'position': 'relative', // необходимо для нормального отображения в ИЕ6(7)
                'overflow': 'hidden', // прячем все, что не влезает в контейнер
                'margin-left': 'auto',
                'margin-right': 'auto',
                'width': getVisibleWidth()
            });
            //вычисляем расстояние отупа от каждого элемента
            $carousel.css({
                'position': 'relative', // разрешаем сдвиг по оси
                'width': 9999 + 'px', // увеличиваем лену карусели
                'left': 0
            });

//прокрутка карусели в наравлении dir [true-вперед; false-назад]
            function slide(dir) {
                var direction = !dir ? -1 : 1, // устанавливаем заданное направление
                    Indent = 0, // смещение (для ul)
                    moveItems, moveWidth;
                if (!running) {
                    // если анимация завершена (или еще не запущена)
                    running = true; // ставим флажок, что анимация в процессе
                    if (intID) { // если запущен интервал
                        window.clearInterval(intID); // очищаем интервал
                    }
                    if (!dir) { // кнопка "Предыдущий"
                        moveItems = $carousel.children().slice(0, settings.rotateBy);
                        $carousel.children(':last').after(moveItems.clone(true));
                        moveWidth = getSumWidth(moveItems);
                    } else { // кнопка "Следующий"
                        moveItems = $carousel.children().slice(itemsTotal - settings.rotateBy, itemsTotal);
                        $carousel.children(':first').before(moveItems.clone(true));
                        moveWidth = getSumWidth(moveItems);
                        $carousel.css('left', -moveWidth + 'px')
                    }

                    /*
                     * расчитываем  смещение
                     */
                    Indent = parseInt($carousel.css('left')) + moveWidth * direction;
                    var animate_data = {'left': Indent};
// запускаем анимацию
                    $carousel.animate(animate_data, {
                        queue: false,
                        duration: settings.speed,
                        complete: function () {
                            // когда анимация закончена
                            if (!dir) { // если мы мотаем к следующему элементу (так по умолчанию)
                                // удаляем столько первых элементов, сколько задано в rotateBy
                                $carousel.children().slice(0, settings.rotateBy).remove();
                                // устанавливаем сдвиг в ноль
                                $carousel.css('left', 0);
                            } else { // если мотаем к предыдущему элементу
                                // удаляем столько последних элементов, сколько задано в rotateBy
                                $carousel.children().slice(itemsTotal, itemsTotal + settings.rotateBy).remove();
                            }
                            $this.animate({'width': getVisibleWidth()}, {
                                queue: false,
                                duration: 300
                            });
                            if (settings.auto) { // если карусель должна проматываться автоматически
                                // запускаем вызов функции через интервал времени (auto)
                                intID = window.setInterval(function () {
                                    slide(settings.dirAutoSlide);
                                }, settings.auto);
                            }
                            running = false; // отмечаем, что анимация завершена
                        }
                    });
                }
                return false; // возвращаем false для того, чтобы не было перехода по ссылке
            }

// назначаем обработчик на событие click для кнопки "вперед"
            $(settings.btnNext).click(function () {
                return slide(false);
            });
            // назначаем обработчик на событие click для кнопки "Назад"
            $(settings.btnPrev).click(function () {
                return slide(true);
            });

            if (settings.auto) { // если карусель должна проматываться автоматически
                // запускаем вызов функции через временной интервал
                intID = window.setInterval(function () {
                    slide(settings.dirAutoSlide);
                }, 3000);
            }
        });
    };
})(jQuery);