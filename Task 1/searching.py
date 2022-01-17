import re


_EMAIL_PATTEN = r'([\w.-]+)@([\w-]+)\.(\w+)(\.pk)?'
_DATE_PATTERN = r'(\d{2,4})[-\/.](\d{1,2})[-\/.](\d{1,2})'
_NUMBER_PATTERN = r'\(?\+?(\d{3})\)?[\-\s](\d{3})[-\s](\d{4})'


def _find_matches(pattern, str_to_search):
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.finditer(str_to_search)

    matches_list = [match.group(0) for match in matches]
    return matches_list


def extract_emails(str_to_search):
    return _find_matches(_EMAIL_PATTEN, str_to_search)


def extract_dates(str_to_search):
    return _find_matches(_DATE_PATTERN, str_to_search)


def extract_numbers(str_to_search):
    return _find_matches(_NUMBER_PATTERN, str_to_search)
