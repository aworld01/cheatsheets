import re

def cleaner(arg):
    """Enhanced regex pattern to fully remove the sequence number and timestamp"""
    pattern = r"^\s*\d+\s*\n\s*\d{2}:\d{2}:\d{2},\d{3} --> \s*\d{2}:\d{2}:\d{2},\d{3}\s*\n"

    """Using re.sub to clean the text"""
    cleaned_text = re.sub(pattern,"",data,flags=re.MULTILINE)
    return cleaned_text

if __name__ == "__main__":
    """Read data from the file"""
    with open("data.srt","r",encoding="utf-8-sig") as rf:
        data = rf.read()
    # print(repr(data))

    """Print output"""
    cleaned_text = cleaner(data)
    cleaned_text = cleaned_text.replace("\n"," ")
    print(cleaned_text)

    """save output"""
    with open("cleaned_data.txt","w",encoding="utf-8") as wf:
        wf.write(cleaned_text)