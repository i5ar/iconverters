HyperText Markup Language to reStructuredText:

	>>> pandoc stress.html -f html -t rst -o stress.rst

reStructuredText to HyperText Markup Language:

    >>> pandoc stress.rst -f rst -t html -s -o stress.html
