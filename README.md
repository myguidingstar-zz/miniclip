Miniclip
========

A Linux tray app that quickly converts HTML to Jade, CSS to Stylus and JS to Coffee from clipboard. A handy tool for Web developers.

Why Miniclip?
=============
I'm a fan of minimalist things like [Jade](http://jade-lang.com/), [Stylus](http://learnboost.github.com/stylus/) and [CoffeeScript](http://coffeescript.org/).

Sometimes when surfing the web you may found some interesting HTML/CSS/JS snippets... and you want them to be short :)

Installation
============
You need a Linux with [Python](http://www.python.org/) and [Nodejs](http://nodejs.org/) installed.
Miniclip uses some nodejs's command-line tools that need to be installed globally. (You only have to install which you want, not all of them!)

  * Install [html2jade](https://github.com/donpark/html2jade)

```
npm install -g contextify
npm install -g html2jade
```
  * Install stylus

```
npm install -g stylus
```

  * Install [js2coffee](http://js2coffee.org/)

```
npm install -g js2coffee
```

Note on Ubuntu users:
--------------------
Ubuntu users with Unity desktop may have the problem of "missing system tray icons". In this case, please check the quick solution [here](https://github.com/myguidingstar/miniclip/issues/1)

Usage
=====
The GUI (miniclip.py)
---------------------

Try scrolling around Twitter [bootstrap](http://twitter.github.com/bootstrap/scaffolding.html), copy the code snippets there and see the results.

The CLI (cli.py)
----------------
The CLI version is intended to be used with system's global shortcuts. 
You can assign GNOME, KDE etc shortcuts to some commands. 
Please run with `-h` option to see more usage.

License
=======
The [GPL License v3](http://www.gnu.org/licenses/gpl.html)

Copyright (c) 2012 Hoang Minh Thang
