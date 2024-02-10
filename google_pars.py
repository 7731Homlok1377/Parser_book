try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "благословение небожителей 4 библио глобус"

for j in search(query, tld="co.in", num=10, stop=3, pause=2):
    print(j)

