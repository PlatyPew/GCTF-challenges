var website = '127.0.0.1';

var system = require("system");

input = escape(system.args[1]);

var page = require('webpage').create();

phantom.addCookie({
	'name'     : 'passwordzzzzz', 
	'value'    : '1_4m_z3_4dm1n_0f_z15_5173_pl3453_n0_h4ck_d4nk', 
	'domain'   : website,
});

page.open("http:" + website + "/showImage.php?url=" + input ,function (status) {
	console.log(page.content);
	phantom.exit(0)
});
