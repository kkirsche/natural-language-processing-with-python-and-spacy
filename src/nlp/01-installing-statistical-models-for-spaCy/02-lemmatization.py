from spacy import load


def main() -> None:
    """Run the tokenization function.

    Install en_core_web_md via:
    poetry run python -m spacy download en_core_web_md

    >>> main()
    this this
    product product
    integrates integrate
    both both
    libraries library
    for for
    downloading download
    and and
    applying apply
    patches patch
    """
    nlp = load(name="en_core_web_md")
    document = nlp(
        text=(
            "this product integrates both libraries for downloading and "
            + "applying patches"
        )
    )
    for token in document:
        # lemma_ is the string
        # lemma is the integer
        print(token.text, token.lemma_)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
