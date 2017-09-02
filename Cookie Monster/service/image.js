var system = require("system");

input = escape(system.args[1]);

var page = require('webpage').create();

phantom.addCookie({
	  'name'     : 'flag', 
	  'value'    : 'GCTF{c_15_f0r_c00k13_4nd_c00k13_15_f0r_m3}', 
	  'domain'   : '192.168.159.131',
});

page.open("http://192.168.159.131/showImage.php?url=" + input ,function (status) {
	console.log(page.content);
	phantom.exit(0)
});
