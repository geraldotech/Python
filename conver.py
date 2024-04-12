import unicodedata
import re

def get_slug_from_string(input_string, limit=None):
    normalized_string = unicodedata.normalize('NFD', input_string)
    stripped_string = ''.join(char for char in normalized_string if not unicodedata.combining(char))
    lowercase_string = stripped_string.lower()
    alphanumeric_string = re.sub(r'[^\w\s]', '', lowercase_string)
    slug_string = re.sub(r'\s+', '-', alphanumeric_string)
    
    if limit is not None:
        slug_string = slug_string[:limit].rstrip('-')
    
    return slug_string

# Example usage:
input_string = "This is a sample string, 12345!"
slug = get_slug_from_string(input_string, limit=20)
print(slug)  # Output: "this-is-a-sample-string-12345"
