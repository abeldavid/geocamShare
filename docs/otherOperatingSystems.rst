=========================================
Other Operating Systems
=========================================

Mac OS X
~~~~~~~~

The most straightforward (if slow) way to install the non-Python
dependencies of Share under Mac OS X is using `MacPorts`_. After you've
installed MacPorts, here's a command that installs the more vital
dependencies::

  sudo port -vn install py27-virtualenv py27-pip git-core sqlite3 jpeg p5-image-exiftool 
  sudo port select python python27

.. _MacPorts: http://www.macports.org

If you are just starting with MacPorts, note that that command will
install a massive software stack including both Python and Perl
interpreters, and could take hours of compilation time. Once you've
installed it, you will want to make sure ``/opt/local/bin`` is in
your PATH and you're using the MacPorts Python 2.7 interpreter.

An additional set of dependencies is needed to render the map marker
icons from SVG source files.  You can either install those dependencies
(another large software stack including X11)::

  sudo port -vn install ImageMagick

Or you can install pre-rendered icons instead::

  cd $GEOCAM_DIR/geocamShare
  curl http://geocamshare.org/downloads/geocamLensRenderedIcons-2011-08-11.tgz -O
  tar xvfzm geocamLensRenderedIcons-2011-08-11.tgz

(Note the 'm' option to tar instructs it to set the mtime of the
extracted files to the current time instead of the mtime stored in the
archive. That way the the pre-rendered icons will be newer than the
source icons and the rendering script will not try to regenerate them.)

| __BEGIN_LICENSE__
| Copyright (C) 2008-2010 United States Government as represented by
| the Administrator of the National Aeronautics and Space Administration.
| All Rights Reserved.
| __END_LICENSE__
