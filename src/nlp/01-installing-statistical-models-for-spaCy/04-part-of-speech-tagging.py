from spacy import load
from spacy.symbols import LEMMA, ORTH


def main() -> None:
    """Run the tokenization function.

    Install en_core_web_md via:
    poetry run python -m spacy download en_core_web_md

    >>> main()
    ['I', 'have', 'fly', 'to', 'LA', '.', 'now', 'I', 'be', 'fly', 'to', 'San Francisco', '.']
    """
    nlp = load(name="en_core_web_md")
    special_case = [{ORTH: "Frisco"}]
    special_attrs = {LEMMA: "San Francisco"}
    nlp.tokenizer.add_special_case("Frisco", special_case)
    ruler = nlp.get_pipe("attribute_ruler")
    ruler.add(patterns=[special_case], attrs=special_attrs)  # type: ignore[attr]
    document = nlp(text="I have flown to LA. Now I am flying to Frisco.")
    print([token.lemma_ for token in document])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
