# Contribution Guidelines

**Please ensure your pull request adheres to the following guidelines**:

* Use `.md` or `.rst` for the documentation.
* Please make an individual commit for each suggestion in a pull request.

### Consider using [Pandoc] for convertions

HyperText Markup Language to reStructuredText:

	>>> pandoc stress.html -f html -t rst -o stress.rst

reStructuredText to HyperText Markup Language:

    >>> pandoc stress.rst -f rst -t html -s -o stress.html


**Thank you for your suggestions**!

[Pandoc]: http://johnmacfarlane.net/pandoc/
