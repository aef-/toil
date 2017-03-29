Toil
====

Toil is an open-source pure-Python workflow engine that lets people write better
pipelines. You can:

* Write your workflows in `Common Workflow Language`_ (CWL)
* Run workflows on your laptop or on huge commercial clouds such as
  `Amazon Web Services`_ (including the `spot market`_), `Microsoft Azure`_,
  `OpenStack`_, and `Google Compute Engine`_
* Take advantage of high-performance computing environments with batch systems
  like `GridEngine`_, `Apache Mesos`_, and `Parasol`_
* Run workflows concurrently at scale using thousands of nodes, managed by Toil's :ref:`Autoscaling` capabilities
* Execute workflows efficiently with caching and resource requirement specifications
* Easily link databases and services

Toil is, admittedly, not quite as good as sliced bread, but it's about as close
to it as you're gonna get.

Check out our `website`_ for a more comprehensive list of Toil's features, read
our `paper`_ to learn more about what Toil can do in the real world, or jump in
and start with the :ref:`installation-ref` section. (Feel free to also join us
on `GitHub`_ and `Gitter`_.)

.. _website: http://toil.ucsc-cgl.org/
.. _GridEngine: http://gridscheduler.sourceforge.net/
.. _Parasol: http://genecats.soe.ucsc.edu/eng/parasol.html
.. _Apache Mesos: http://mesos.apache.org/
.. _spot market: https://aws.amazon.com/ec2/spot/
.. _Microsoft Azure: https://azure.microsoft.com
.. _Amazon Web Services: https://aws.amazon.com/
.. _Google Compute Engine: https://cloud.google.com/compute/
.. _OpenStack: https://www.openstack.org/
.. _GitHub: https://github.com/BD2KGenomics/toil
.. _Gitter: https://gitter.im/bd2k-genomics-toil/Lobby
.. _paper: http://biorxiv.org/content/early/2016/07/07/062497

Getting Started
~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   install/basic
   running/running
   install/cloud
   running/cloud

User Guide
~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   cli
   developing
   deploying

API and Architecture
~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   toilAPI
   architecture
   batchSystem
   jobStore

Contributor's Guide
~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   contributing/contributing

Indices and tables
~~~~~~~~~~~~~~~~~~

* :ref:`genindex`
* :ref:`search`
