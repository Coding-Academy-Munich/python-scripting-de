# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Das `requests` Package</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Das `requests` Package
#
# Das Python Package `requests` bietet
# [viele Features](https://requests.readthedocs.io/en/latest/#beloved-features)
# für den Umgang mit RESTful APIs:
#
# - Keep-Alive & Connection Pooling
# - Internationale Domains und URLs
# - Sessions mit Cookie Persistence
# - Browser-style SSL Verifikation
# - Automatisches Content Decoding
# - Basic/Digest Authentication
# - Elegante Key/Value Cookies
# - Automatische Dekompression
# - Unicode Response Bodies
# - HTTP(S) Proxy Support
# - Multipart File Uploads
# - Streaming Downloads
# - Connection Timeouts
# - Chunked Requests
# - `.netrc` Support


# %% [markdown]
#
# ## GET Requests
#
# Wir rufen Daten von der [JSON Placeholder](https://jsonplaceholder.typicode.com/)
# Website ab.

# %%
import requests

# %% [markdown]
#
# Der folgende Request gibt ein Item zurück:

# %%
url = "https://jsonplaceholder.typicode.com/posts/1"

# %%
response = requests.get(url)

# %%
response

# %%
response.status_code

# %%
response.headers

# %%
response.headers["Content-Type"]

# %%
response.content

# %%
response.json()

# %%
response.raise_for_status()

# %% [markdown]
#
# Der folgende Request gibt mehrere Items zurück:

# %%
posts_url = "https://jsonplaceholder.typicode.com/posts"

# %%
post_request = requests.get(posts_url)

# %%
len(post_request.json())

# %%
limited_request = requests.get(posts_url, data={})

# %% [markdown]
#
# ## Fehlerbehandlung

# %%
missing = requests.get("https://example.com/does-not-exist")

# %%
missing.status_code

# %%
missing.headers

# %%
missing.headers["Content-Type"]

# %%
missing.content

# %%
# missing.raise_for_status()


# %% [markdown]
#
# ## Beispiel: Länder-Informationen

# %%
import requests


# %%
def print_info_for_single_country(data):
    received_name = data["name"]["common"]
    country_code = data["cca2"]
    capital = data["capital"][0]
    population = data["population"]

    # Print the country data
    print("=" * 48)
    print(f"Country name: {received_name}")
    print(f"Country code: {country_code}")
    print(f"Capital:      {capital}")
    print(f"Population:   {population}.")


# %%
# Set the API endpoint URL and the name of the country you want to retrieve data for
country_url = "https://restcountries.com/v3.1/name/"


# %%
def print_country_info(country_name):
    # Send the API request and retrieve the response
    response = requests.get(country_url + country_name)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python list
        data = response.json()

        # Print the country data
        print(f"When searching for {country_name}:")
        for country in data:
            print_info_for_single_country(country)
    else:
        # If the request was not successful, print an error message
        print(f"Error {response.status_code}: {response.reason}")


# %%
print_country_info("United States")


# %%
def get_country_info(country_name):
    response = requests.get(country_url + country_name)
    response.raise_for_status()
    assert response.headers["Content-Type"] == "application/json"
    return response.json()


# %%
get_country_info("Germany")

# %%
for country in get_country_info("Germany"):
    print_info_for_single_country(country)

# %%
try:
    get_country_info("Nowhere")
except requests.HTTPError as err:
    print(err)

# %% [markdown]
#
# ## Mini-Workshop: Abfrage von Produkten
#
# Die Website [https://dummyjson.com/] stellt JSON-Daten für Testzwecke bereit.
#
# Unter der URL [https://dummyjson.com/products] können Sie mit einem
# GET-Request die Daten von 30 Produkten im JSON-Format abrufen. Jedes Produkt
# hat dabei die folgende Form:
#
# ```python
#  {"id": 1,
#   "title": "...",
#   "description": "...",
#   "price": 123,
#   "discountPercentage": 1.23,
#   "rating": 1.23,
#   "stock": 123,
#   "brand": "...",
#   "category": "...",
#   "thumbnail": "http://example.com/img",
#   "images": ["http://example.com/foo", "http://example.com/bar"]
#  }
# ```
#
# Die Liste mit Produkten ist in einem JSON-Objekt mit dem Attribut `products`
# zurückgegeben. Das vom GET-Request zurückgegebene Objekt hat also die Form
#
# ```python
# {"products": [{"id": 1, ...}, ..., {"id": 99, ...}]}
# ```
# Schreiben Sie eine Funktion `get_products()`, die diese Produkte zurückgibt.

# %%
product_url = "https://dummyjson.com/products"


# %%
def get_products():
    result = requests.get(product_url)
    result.raise_for_status()
    return result.json()["products"]


# %%
results = get_products()

# %%
len(get_products())


# %% [markdown]
#
# Schreiben Sie eine Funktione `get_single_product(id: int)`, die das Produkt
# mit ID `id` zurückgibt.

# %%
def get_single_product(id: int):
    result = requests.get(f"{product_url}/{id}")
    result.raise_for_status()
    return result.json()


# %%
get_single_product(1)


# %%
def search_product(query: str):
    result = requests.get(f"{product_url}/search", params={"q": query})
    result.raise_for_status()
    return result.json()["products"]


# %%
[p["title"] for p in search_product("phone")]


# %% [markdown]
#
# ### Ende des Workshops

# %% [markdown]
#
# POST und PUT Requests

# %%
posts_url = "https://jsonplaceholder.typicode.com/posts"

# %%
new_post = {
    "userId": 10,
    "title": "My new posts",
    "body": "This is the contents",
}

# %%
post_response = requests.post(posts_url, data=new_post)

# %%
post_response.status_code

# %%
post_response.json()

# %%
# requests.get(posts_url + "/101")

# %%
patch_response = requests.patch(posts_url + "/1", data={"title": "A new title"})

# %%
patch_response.status_code

# %%
patch_response.json()

# %%
