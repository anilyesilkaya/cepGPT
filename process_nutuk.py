import argparse
import ebooklib
import re
from pathlib import Path
from ebooklib import epub
from bs4 import BeautifulSoup

def process_text(text):
    # Strip all UNICODE control characters
    text = re.sub(r"\x01", "", text)

    # Replace three and more linebreaks with double linebreak
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Handling the section titles broken into two lines
    text = re.sub(r"\n\s{3,3}", "", text)

    # Handling the text decoration
    text = re.sub(r"\s\(\…\)", "", text)
    text = re.sub(r"\s…", "", text)
    text = re.sub(r"…+\.+", ".", text)
    text = re.sub(r"…{2,}", "\n", text)
    text = re.sub(r"…", "...", text)

    return text

def main() -> None:
    parser = argparse.ArgumentParser(description="Dataset analyzer")
    parser.add_argument("--input", required=True, help="Relative path for the EPUB file")
    parser.add_argument("--output", required=True, help="Relative path for the processed file")
    args = parser.parse_args()

    # Fetch the user inputs
    in_file = args.input
    out_path = args.output

    # Load the EPUB file
    book = epub.read_epub(Path(in_file))
    
    # Iterate through the sections of the book
    for idx, item in enumerate(book.get_items()):
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text() #raw text
            
            # Process text (if needed)
            proc_text = process_text(text)
            print(proc_text)
            
            # Save the text into a txt file
            with open(Path(out_path,"nutuk.txt"), "a", encoding="utf-8") as f:
                f.writelines(proc_text)    

if __name__=="__main__":
    main()