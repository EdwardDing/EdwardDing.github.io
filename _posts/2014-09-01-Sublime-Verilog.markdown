---
layout: post
title: "Verilog on Sublime Text 2"
data: 2014-09-01 10:13:00
excerpt: "This post will only exist for 24 hours then deleted automatically. Take your time Guoxiang Han, an d enjoy your life in UCB"
---

###Install Sublime Text 2

---------------------
This should be easy, just download [here](http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2.dmg).

###Install Package Control

---------------------
Package Control is an add-on for ST2, that maitains all your packages automatically. With Package Control, you won't need to maintain the source code of add-ons on your own.

To install Package Controll, open ST2, select `View -> show console`, and copy these Python lines below to the input box.

> import urllib2,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')

Hit `return`, wait for a cup of coffe, restart ST2 and Package Control is ready for use.

###Install Verilog Suppot on ST2

---------------------
Press `cmd + shift +p` to open control panel in ST2, and type in `install` then hit `return`. 

Wait for seconds, and your ST2 should be like this:

![screen shot for ST2](/assets/ST_PC.png)

Then, type in the name of the package you want to install like `verilog`. Some possible results will come up soon.

![screen shot for Verilog](/assets/ST_verilog.png)

Install it simply by hit `return`. I'll take the first package which is sytax highlight for Verilog HDL for example.

To use the package you just installed, press `cmd + shift +p` to call up the controll panel and type in `verilog`. 

![syntax](/assets/syntax.png)

Ok, everything is set up now, enjoy your ST2.

![ready2use](/assets/ready2use.png)

###Other Tips

----------------------
If you want to install other packages later, repeat steps above and simply change the package name to search.

One more thing about the themes. Personally, I recommand `Monokai` theme. You can set it in `Prefrences -> Color Scheme -> Color Scheme Default -> Monokai`


###Hope this tutorial helps you my friend, and enjoy your life in UCB :)