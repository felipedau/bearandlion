bearandlion
-----------
This package is inspired by **LIONESS**, a Large Block Cipher
described in the `paper`_ *"Two practical and provably secure block
ciphers: BEAR and LION*" by Ross Anderson and Eli Biham, and
implemented by `Ian Goldberg`_ as part of `Sphinx`_. It should be
considered a fork of the `original implementation`_ released by *Ian
Goldberg* on 2011-03-06. The initial commit of this repository was
adapted from the ``SphinxParams`` module and is currently maintained
by *Felipe Dau* and *David R. Andersen*, as part of Felipe's Senior
Design Project.

This package currently consists only of *LIONESS*, but it is intended
that both *BEAR* and *LION* be implemented as well. The *LIONESS*
implementation and the *xcounter* CTR mode class were adapted by
*Ian Goldberg* from *"Experimental implementation of the sphinx
cryptographic mix packet format"* by `George Danezis`_.

**Please, consider this package in alpha stage and do not use it in a
production environment.**

Cryptography
------------
Most of the cryptographic operations come from `pycrypto`_.

Feedback
--------
Please use the `GitHub issue tracker`_ to leave suggestions, bug
reports, complaints or anything you feel will contribute to this
package.

Contributing
------------
Contributions are more than welcome, and as this package is part of
Felipe's Senior Design Project, all the contributors of this
repository (until the project is concluded) will be mentioned on his
paper.

Acknowledgements
----------------
- Thanks to *David R. Andersen* and *Francisco Pereira Junior* for
  working on the development of this package and for supervising
  Felipe's Senior Design Project

- Thanks to *George Danezis* and *Ian Goldberg* for implementing
  *LIONESS*.

.. _`george danezis`: http://www0.cs.ucl.ac.uk/staff/G.Danezis
.. _`github issue tracker`: https://github.com/felipedau/bearandlion/issues
.. _`ian goldberg`: https://cs.uwaterloo.ca/~iang
.. _`original implementation`: https://crysp.uwaterloo.ca/software/Sphinx-0.8.tar.gz
.. _`paper`: http://link.springer.com/chapter/10.1007%2F3-540-60865-6_48
.. _`pycrypto`: https://pypi.python.org/pypi/pycrypto
.. _`sphinx`: https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf
