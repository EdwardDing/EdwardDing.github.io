---
layout: post
title: "Batch Renamer for OSX with Python"
categories: tutorial
excerpt: A python script for bacth renamer files in Mac OSX.
---

This is just a simple script, but very helpful when you need to automatically rename a bunch of files, especially images from your camera.

If you are a user, just read the first part of this post which is a `How to use` section and download the executable scirpt. If you are a programmer who want to dig out how to implement this, read the second part, which I will explain a little bit about the scirpt and provide a copy of my source code.

###How to use

-----------------------
It is quite easy to use this script, with only 3 steps.

***Step 1: Download and run the script in your terminal***

Open the `Lauchpad` and input `Terminal` in the search field and hit return to open it. Then, drag the script into the terminal window and hit return.

You can download the executable script [here](/assets/renamer.py)


***Step 2: Prepare your input / output folder***

Prepare your input, including all files you want to filter or rename.

<div style="text-align: center">
	<a href="/assets/renamer/input.png">
		<img src="/assets/renamer/input.png" alt="input" height="80%" width="80%"></img>
	</a>
</div>

According to the tips given, drag the input folder into the terminal, then the output folder, like the picure shows.

<div style="text-align: center">
	<a href="/assets/renamer/drag.png">
		<img src="/assets/renamer/drag.png" alt="drag" height="80%" width="80%"></img>
	</a>
</div>

Then, input the file extension you want to filter. For example, if just want to rename all .png pictures, you may input png and hit return. (No need to input '.'). Multiple extensions is also supported, separated by ','.

When you finish, your terminal should be something look like this:

<div style="text-align: center">
	<a href="/assets/renamer/finish.png">
		<img src="/assets/renamer/finish.png" alt="finish" height="80%" width="80%"></img>
	</a>
</div>

***Step 3: Bazinga!***

There is no step 3 :) When you've done all thing above, all the files already have been renamed from number 1 to number n in your output folder waiting for you. Enjoy!

<div style="text-align: center">
	<a href="/assets/renamer/output.png">
		<img src="/assets/renamer/output.png" alt="output" height="80%" width="80%"></img>
	</a>
</div>

###Script and source code

The script is every easy to implement. Below are my source code:

{% highlight python %}
#!/usr/bin/env python
import os,sys

def renamer(inputFile, outputFile, ext):
	n = 1
	for filename in os.listdir(inputFile):

		file_ext = filename.split('.')[-1]

		if file_ext in ext:
			f = open(inputFile + '/' + filename,'r')

			line = f.read()
			f2 = open(outputFile+ '/' + str(n) + '.' + file_ext,'w')
			f2.write(line)
			n = n + 1
			f.close()
			f2.close()

if __name__ == '__main__':

	print ("\n--------------------------")
	print ("Welcome to DJR Renamer")
	print ("--------------------------\n")

	inputFile = raw_input("Drag the input folder here and hit return: ")
	outputFile = raw_input("Drag the output folder here and hit return: ")
	ext_raw = raw_input("Input the file extension you want to rename automatically\nYou can input multiple extension, separated by ',' (e.g. png,jpg) : ")	

	ext = ext_raw.split(',')
	
	renamer(inputFile.rstrip(), outputFile.rstrip(), ext)

	print "Finished! Enjoy :)"
{% endhighlight %}

It simply iterate all files in your given input folder, get the extension of your files to decide wheter to include it in your output folder. Then, we read the orginal files and make a copy of it in the output files.

You cannot use `filename[filename.find('.'):]` as the name of file may be something like `test.in.txt`.
