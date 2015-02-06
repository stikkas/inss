(function($) {
    $(document).ready(function(){
        window.adjustHeight = function(min_height) {
            var MIN_HEIGHT = min_height || 700;
            var windowHeight = $(window).outerHeight() - 1;
            var siteHeight = $('.layout-base').outerHeight();
            var leftPanel = $('.content__side-panel');
            var workspace = $('.workspace');
            var workspaceBody = $('.workspace__body');

            /* Stretch site by height */
            if (siteHeight < windowHeight) {
                workspaceBody.height(workspaceBody.height() + (windowHeight - siteHeight));
            }

            /* Cut height */
            if (siteHeight > windowHeight && siteHeight > MIN_HEIGHT) {
                if (MIN_HEIGHT > windowHeight) {
                    workspaceBody.height(workspaceBody.height() - (siteHeight - MIN_HEIGHT));
                } else {
                    workspaceBody.height(workspaceBody.height() - (siteHeight - windowHeight));
                }
            }

            /* Align left-panel and workspace by height */
            if (leftPanel.outerHeight() > workspace.outerHeight()) {
                workspaceBody.height(workspaceBody.height() + (leftPanel.outerHeight() - workspace.outerHeight()));
            }

        };
        window.adjustHeight();
        $(window).resize(function(){ window.adjustHeight() });
    });
})(window.jQuery);
