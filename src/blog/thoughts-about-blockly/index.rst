Thoughts about blockly
======================

Recently I had one of my many hissy fits about the disjointed state of software
development and how trivial apps actually take a lot of effort to develop and
deploy (probably more to deploy actually). Inevitably ended up wandering the
realm of visual programming languages in the hope that humanity have finally
invented a system for software development that isn't completely awful.

Needless to say I didn't find what I wanted but I found
`blockly <https://developers.google.com/blockly/>`_. It's a nifty
library for "represents coding concepts as interlocking blocks". It's very
similar to scratch so if you are familiar with that project like I was, you'll
feel right at home, if you are not, it's a visual programming language that
allows you to develop quite a varied type of programs without much too hassle.

There are many good things to be said about blockly, since it's a javascript
project, it can be easily embedded into whatever web application you want to
develop, since it's web, most people will be familiar with the development and
customization process.

When I tried using it I have felt that some good stuff that could be used to
write programs was missing, most importantly functions for accessing the
browser attributes and procedures. So I created a few things and uploaded my
version of blockly, live version `here <https://msl09.com.br/cody/>`_ and code
`here <https://msl09.com.br/cody/>`_.

All is nice and well but there are a few problems with it:

- Since blockly can target many languages, it's not particularly good at any
  or make use of the more specific super-powers of any language.
- Because the people at google wanted to keep things simple the programs you
  make with it won't have local scope variables.
- The
  `meta block editor <https://blockly-demo.appspot.com/static/demos/blockfactory/index.html>`_
  (developer tools) is not capable of saving your work
  directly to the OS (since it's a html library)
- Again regarding the block editor it was incapable of creating blocks with
  mutators at the last time I played with it (2017-06-15).

Regardless it's a fun little project that I enjoyed playing with it a lot.
Solving simple programming challenges with it was a brought me a joy that I
have mostly forgotten since I left college. I cannot help but wish to work more
with it and develop some integration with some tool like
`ansible <https://www.ansible.com/>`_ or `puppet <https://puppet.com/>`_ or
actually give it full IDE powers but this experiment was enough sidetracking
for me now.