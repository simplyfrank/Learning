define(function(){
    var cache = {};

    return {
        pub: function(id){
            // call applies the function on the object, so it becomes an array that we can slice
            // Thereby invoking the current context and passing it on, together with all arguments after position 1
            var args =[].slice.call(arguments, 1);

            if (!cache[id]){
                cache[id]=[];
            }
            // We iterate trough all provided functions, using the apply to invoke them(setting context to null)
            // apply allows us to call a function with an array, without having to pass them as comma seperated list
            for (var i = 0, il = cache[id].length; i < il; i++){
                cache[id][i].apply(null, args);
            }
        },
        sub: function(id, fn){
            // If cache not yet set, initialize it and store the function with the key of id
            if(!cache[id]){
                cache[id]=[fn];
            } else {
                // else: append the callback-function on the object
                cache[id].push(fn);
            }
        }
    }
});