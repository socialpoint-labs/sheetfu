How to contribute to Sheetfu
============================

(this is pretty much a copy of the Flask contribution documentation).

Thank you for considering contributing to Sheetfu! This is a very young library,
easy to understand, where lots can be added.


Support questions
-----------------

For questions about your own code ask on `Stack Overflow`_. Search with
Google first using:
  ``site:stackoverflow.com sheetfu {search term, exception message, etc.}``

.. _Stack Overflow: https://stackoverflow.com/questions/tagged/sheetfu?sort=linked


Reporting issues
----------------

Use the issue tracker for this:

- Describe what you expected to happen.
- If possible, include a `minimal, complete, and verifiable example`_ to help
  us identify the issue. This also helps check that the issue is not with your
  own code.
- Describe what actually happened. Include the full traceback if there was an
  exception.
- List your Python and Sheetfu version.

.. _minimal, complete, and verifiable example: https://stackoverflow.com/help/mcve

Submitting patches
------------------

- Include tests if your patch is supposed to solve a bug, and explain
  clearly under which circumstances the bug happens. Make sure the test fails
  without your patch.
- Try to follow `PEP8`_.
- Use the utils at your disposition in test folders to mock api requests.
- Every mock request should be put in the fixture folder.
- Tests are run with pytest.

First time setup
~~~~~~~~~~~~~~~~

- Download and install the `latest version of git`_.
- Configure git with your `username`_ and `email`_::

        git config --global user.name 'your name'
        git config --global user.email 'your email'

- Make sure you have a `GitHub account`_.
- Fork Sheetfu to your GitHub account by clicking the `Fork`_ button.
- `Clone`_ your GitHub fork locally::

        git clone https://github.com/{username}/sheetfu
        cd sheetfu

- Add the main repository as a remote to update later::

        git remote add socialpoint-labs https://github.com/socialpoint-labs/sheetfu
        git fetch socialpoint-labs

- Create a virtualenv::

        python3 -m venv env
        . env/bin/activate
        # or "env\Scripts\activate" on Windows

- Install Sheetfu in editable mode with development dependencies::

        pip install -e ".[dev]"

.. _GitHub account: https://github.com/join
.. _latest version of git: https://git-scm.com/downloads
.. _username: https://help.github.com/articles/setting-your-username-in-git/
.. _email: https://help.github.com/articles/setting-your-email-in-git/
.. _Fork: https://github.com/socialpoint-labs/sheetfu/fork
.. _Clone: https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork

Start coding
~~~~~~~~~~~~

- Create a branch to identify the issue you would like to work on (e.g.
  ``2287-dry-test-suite``)
- Using your favorite editor, make your changes, `committing as you go`_.
- Try to follow `PEP8`_.
- Include tests that cover any code changes you make. Make sure the test fails
  without your patch.
- Push your commits to GitHub and `create a pull request`_.
- Celebrate 🎉

.. _committing as you go: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
.. _PEP8: https://pep8.org/
.. _create a pull request: https://help.github.com/articles/creating-a-pull-request/


Running the tests
~~~~~~~~~~~~~~~~~

Run the basic test suite with::

    pytest

This only runs the tests for the current environment. Travis-CI will run the full
suite when you submit your pull request.


Running test coverage
~~~~~~~~~~~~~~~~~~~~~

Generating a report of lines that do not have test coverage can indicate
where to start contributing. Run ``pytest`` using ``coverage`` and generate a
report on the terminal and as an interactive HTML document::

    coverage run -m pytest
    coverage report
    coverage html
    # then open htmlcov/index.html

Read more about `coverage <https://coverage.readthedocs.io>`_.


make targets
~~~~~~~~~~~~

Sheetfu provides a ``Makefile`` with various shortcuts. They will ensure that
all dependencies are installed.

- ``make test`` runs the basic test suite with ``pytest``
- ``make cov`` runs the basic test suite with ``coverage``
