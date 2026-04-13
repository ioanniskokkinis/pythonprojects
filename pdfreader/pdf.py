import hashlib
import difflib
from difflib import SequenceMatcher, get_close_matches

with open("my_document.pdf", "rb") as f:
    file_hash = hashlib.file_digest(f, "sha256").hexdigest()

content = ["startup", "technology", "python", "innovation"] 

na = input("Tell me one word to search: ").lower()

matches = get_close_matches(na, content, n=1, cutoff=0.6)

if matches:
    similarity = SequenceMatcher(None, na, matches[0]).ratio()
    print(f"Close match found: '{matches[0]}' (Similarity: {similarity:.2%})")
else:
    print("No close match found.")
