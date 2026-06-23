def markdown_to_blocks(markdown):
    splitted = markdown.split("\n\n")
    print(splitted)
    result = []
    for i in splitted:
        i = i.strip()
        if len(i) > 0:
            result.append(i)
    return result
