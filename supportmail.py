##! python3
# https://www.nltk.org/book/
# https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3


from pathlib import Path
import extract_msg
from nltk.corpus import stopwords
from nltk.probability import FreqDist


def main():

    # create list of emails in folder

    fpath = (
        Path.home()
        / "Documents\IFS\\temp"
        / "Copy of #159854# (CASE - 1584490 - 1 - A1) - 1.MSG"
    )

    # read through specific emails
    msg = extract_msg.Message(fpath)
    tokens = msg.body.split()
    sr = stopwords.words("english")
    clean_tokens = [tokens.remove(token) for token in tokens if token in sr]
    freq = FreqDist(clean_tokens)

    # print(tokens)
    print(clean_tokens)

    """
    print(f"From:\t\t{msg.sender}")
    print(f"Subject:\t{msg.subject}")
    print(f"{msg.body.split()}")
    msg.sub
    """

    # try to determine the content matter

    # match email content with keywords
    # suggest course of action


if __name__ == "__main__":
    main()
