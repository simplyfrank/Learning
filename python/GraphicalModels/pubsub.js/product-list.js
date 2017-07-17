define(['./pusub', 'jquery'], function(pubsub, $){
    return {
        init: function(){
            cartCount = 0;

            productList.on('click', 'i', function() {
                var $this = $(this),
                li;

                if ($this.hasClass('icon-plus')){
                    carCount++;

                    $this.removeClass('icon-plus')
                    .addClass('')
                }
            })
        };
    };
});