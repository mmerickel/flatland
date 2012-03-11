.. -*- fill-column: 78 -*-

=======
Signals
=======

.. note::

  This feature is experimental.

Flatland can notify your code when events of interest occur during
flatland processing.  These signals can be used for advanced
customization in your application or simply as a means for tracing and
logging flatland activity during development.

Using Signals
-------------

To receive a signal, all you need is a function that can accept
keyword arguments::

  >>> def receiver(**kw):
  ...   print "Look what I got!", kw
  ...

Receiving functions are :meth:`connected
<flatland.util.signals.Signal.connect>` to one or more signals you'd
like to receive::

  >>> from flatland import signals
  >>> signals.validator_validated.connect(receiver)

That's it.  Now each time flatland runs a validator, the ``receiver``
function will be called and passed some information about the
validation that just occurred.  There is no limit to the number of
receivers connected to a signal.

Built-In Signals
----------------

.. autodata:: flatland.signals.validator_validated