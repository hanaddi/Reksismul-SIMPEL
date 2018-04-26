
<canvas id="myCanvas" width="640px" height="480px" style="border:1px solid #000000;">
	Your browser does not support the canvas element.
</canvas>

<script>
/*
https://www.html5rocks.com/en/tutorials/websockets/basics/
https://www.tutorialspoint.com/websockets/websockets_handling_errors.htm
*/
// var connection = new WebSocket('ws://html5rocks.websocket.org/echo', ['soap', 'xmpp']);

var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');

var connection = new WebSocket('ws://<?php echo ($_SERVER["HTTP_HOST"]); ?>:10333/live'),
stream;
connection.onopen = function () {

	var live = function(){
		connection.send('r');
	}
	stream = window.setInterval (live,100);
	// connection.send('r');

};

connection.onclose = function (error) {
	window.clearInterval(stream);
};

// Log errors
connection.onerror = function (error) {
	console.log('WebSocket Error ' + error);
};

// Log messages from the server
connection.onmessage = function (e) {
	// console.log('Server: ' + e.data);
	// console.log('Server: ');
	try{
		matrix = JSON.parse(e.data);
		for (i in matrix){
			for (j in matrix[i]){
				ctx.fillStyle = "rgb("+c(matrix[i][j][2])+","+c(matrix[i][j][1])+","+c(matrix[i][j][0])+")";
				ctx.fillRect(i*4, j*4, 4, 4);
			}
		}
	}catch(err){
		// console.log(err);
	}
};

function c(a){
	return a
}

</script>

<?php
// var_dump($_SERVER);


?>