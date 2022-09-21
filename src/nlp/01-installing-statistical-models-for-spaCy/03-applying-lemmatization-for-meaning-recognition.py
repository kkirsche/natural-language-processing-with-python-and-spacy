from spacy import load
from spacy.symbols import ORTH, LEMMA


def main() -> None:
    """Run the tokenization function.

    Install en_core_web_md via:
    poetry run python -m spacy download en_core_web_md

    >>> main()
    ['I', 'am', 'flying', 'to', 'Frisco']
    ['I', 'be', 'fly', 'to', 'San Francisco']
    """
    text = "I am flying to Frisco"
    nlp = load(name="en_core_web_md")
    document = nlp(text=text)
    print([token.text for token in document])
    special_case = [{ORTH: "Frisco"}]
    special_attrs = {LEMMA: "San Francisco"}
    nlp.tokenizer.add_special_case("Frisco", special_case)
    ruler = nlp.get_pipe("attribute_ruler")
    ruler.add(patterns=[special_case], attrs=special_attrs)  # type: ignore[attr]
    document2 = nlp(text=text)
    print([token.lemma_ for token in document2])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
