def search(items, query):
    """Return items that contain the query, ignoring case."""
    query = query.casefold()
    return [item for item in items if query in item.casefold()]
