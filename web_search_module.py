import webbrowser

def process_search_command(command):
    search_query = command.replace("search", "").strip()
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)
