var redis = require('redis');

var bluebird = require('bluebird');
bluebird.promisifyAll(redis.RedisClient.prototype);

var grpc = require('grpc');

var hookProto = grpc.load('hook.proto');

var server = new grpc.Server();

var result = {"response":"success"};
console.log(result);

var conn = redis.createClient(6379,"127.0.0.1");

conn.on("connect", function() {
console.log("Redis connected");
});

conn.on("error", function(){
console.log("Error connecting to Redis");
});

var set_hook = function(name,hook) {
conn.set(name,hook,redis.print);
console.log("Set hook success");
}

var get_hook = function(name,callback) {
var result = conn.getAsync(name).then(function(hook) {
	console.log("in get hook -> "+hook)
	return hook;
    });
return Promise.all([result]);
}

server.addService(hookProto.hook.webHook.service, {

	hookCreate: function(call,callback) {
	      console.log(call.request.username,call.request.link);
	      set_hook(call.request.username,call.request.link)
              callback(null,result);
	},
	 
	hookGet: function(call,callback) {
		console.log("in hookGet");
                username = call.request.username;
		console.log(username);
		var output = get_hook(username).then(function(hook){
		console.log("result "+ hook[0]);
		callback(null,{"response":hook[0]});
		});
        }

});

server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
server.start();
