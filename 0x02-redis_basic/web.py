To implement the `get_page` function with caching and tracking URL access counts, you can follow the steps below:

1. Create a new file named `web.py` where you will implement the `get_page` function.
2. Use the `requests` module to fetch the HTML content of a given URL.
3. Track the number of times a specific URL is accessed using a dictionary with keys in the format `count:{url}`.
4. Cache the HTML content with an expiration time of 10 seconds.
5. Implement this functionality using a decorator for caching.

Here is a sample implementation of the `get_page` function with caching and access count tracking using a decorator:

```python
import requests
import time

# Dictionary to store URL access counts
url_access_counts = {}

def cache_with_expiry(seconds):
    def decorator(func):
        cache = {}
        def wrapper(url):
            if url in cache and time.time() - cache[url][1] < seconds:
                return cache[url][0]
            else:
                result = func(url)
                cache[url] = (result, time.time())
                return result
        return wrapper
    return decorator

@cache_with_expiry(10)
def get_page(url):
    global url_access_counts
    if f"count:{url}" in url_access_counts:
        url_access_counts[f"count:{url}"] += 1
    else:
        url_access_counts[f"count:{url}"] = 1

    response = requests.get(url)
    return response.text

# Test the function
url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
print(get_page(url))  # This will fetch the page content and cache it for 10 seconds

# Testing the access count for the URL
print(f"Access count for URL '{url}': {url_access_counts[f'count:{url}']}")

```

In this implementation:
- The `cache_with_expiry` decorator is used to cache the results of the `get_page` function with an expiry time of 10 seconds.
- The `get_page` function fetches the HTML content of a given URL using the `requests` module and increments the access count for that URL.
- The access count is stored in the `url_access_counts` dictionary.
- You can test this implementation by calling `get_page` with a slow URL and checking the access count for that URL.

This implementation should help you achieve the desired functionality of caching and tracking URL access counts in Python.