def escape_all_newline_and_quotes(origin_text: str) -> str:
    return origin_text.encode("unicode_escape").decode("utf8").replace('"', '\\"')
