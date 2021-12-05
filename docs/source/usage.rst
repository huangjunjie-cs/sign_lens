=====
Usage
=====



Command line usage 
-------------------------


.. code-block:: bash

    $ signlens -f tests/test_datas/bitcoin_alpha.edgelist

it will output the metrics for a signed networks

::

    ==========
    +---------------------------------------+----------------------------------+
    |                Metrics                |              Value               |
    +=======================================+==================================+
    | The number of nodes                   | 22650                            |
    +---------------------------------------+----------------------------------+
    | The number of edges                   | 1536                             |
    +---------------------------------------+----------------------------------+
    | Sign distribution (+)                 | 0.936                            |
    +---------------------------------------+----------------------------------+
    | Balanced triangle distribution        | 0.881                            |
    +---------------------------------------+----------------------------------+
    | Unbalanced triangle distribution      | 0.119                            |
    +---------------------------------------+----------------------------------+
    | Signed triangle  (+++, ++-, +--, ---) | (0.8413, 0.1166, 0.0393, 0.0028) |
    +---------------------------------------+----------------------------------+
    | In-degreeoutput                       | output/In-degree.pdf             |
    +---------------------------------------+----------------------------------+
    | In-degree sign output                 | output/In-degree-sign.pdf        |
    +---------------------------------------+----------------------------------+
    | Out-degreeoutput                      | output/Out-degree.pdf            |
    +---------------------------------------+----------------------------------+
    | Out-degree sign output                | output/Out-degree-sign.pdf       |
    +---------------------------------------+----------------------------------+
    | Hop sign output                       | output/Hop.pdf                   |
    +---------------------------------------+----------------------------------+
    | Singular value distribution           | output/Top-K.pdf                 |
    +---------------------------------------+----------------------------------+


Package usage
---------------

Or you can use it by import some class you want to use.

.. code-block:: python

    from sign_lens import SignLens
    model = SignLens('./xxx.edgelist')
    model.report_signed_metrics()

