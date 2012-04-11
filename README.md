## Presence

Simple two-pane presentation software for JessyInk slideshows.

### Why?

It's a very nice thing to be able to see the upcoming slide in your presentation
as you're presenting. JessyInk is a nice way to put together an SVG slideshow,
but using a browser to display the slides doesn't let you as the presenter see
what's coming up. I wrote a little script that uses the Qt WebKit widgets to
display two instances of your slides at once.

### How do I use it?

Download the script, make sure you have Qt 4.7 and the PySide bindings
installed, and then run it as `presence.py <url of your slideshow>`.
