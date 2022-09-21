from spacy import load


def main() -> None:
    """Run the tokenization function.

    Install en_core_web_md via:
    poetry run python -m spacy download en_core_web_md

    >>> main()
    ['I', 'am', 'flying', 'to', 'Frisco']
    """
    nlp = load(name="en_core_web_md")
    document = nlp(text="I am flying to Frisco")
    print([token.text for token in document])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
