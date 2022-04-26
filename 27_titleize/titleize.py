def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    # print(" ".join([p.capitalize() for p in phrase.lower().split(" ")]))
    return " ".join([p.capitalize() for p in phrase.lower().split(" ")])

# titleize('this is awesome')
# titleize('oNLy cAPITALIZe fIRSt')