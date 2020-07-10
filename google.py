import webbrowser

url = "https://www.google.com/search?q="
quation = input("что найти в гугле?\n=>")

webbrowser.open(url+quation)

input()