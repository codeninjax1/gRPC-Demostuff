var redis = require('redis');
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

conn.set("key1","value2",redis.print);
conn.get("key1", function (error,result){
if (error){
console.log(error);
throw error;
}
console.log("GET result ->"+result);
});

conn.append("key1","value2");
conn.del("key1", function (error,result){
if (error){
console.log(error);
throw error;
}
console.log("GET result ->"+result);
});

server.addService(hookProto.hook.webHook.service, {
	hookCreate: function(call,callback) {
	      console.log(call.request.username);
              callback(null,result);
	}

});

server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
server.start();
