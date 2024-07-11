# In this section, i’ll build a web-scraping URL collector, areq.py, using aiohttp, a blazingly fast async HTTP client/server framework. (I just need the client part.) Such a tool could be used to map connections between a cluster of sites, with the links forming a directed graph.

# The high-level program structure will look like this:

# 1.Read a sequence of URLs from a local file, urls.txt.

# 2.Send GET requests for the URLs and decode the resulting content. If this fails, stop there for a URL.

# 3.Search for the URLs within href tags in the HTML of the responses.

# 4.Write the results to foundurls.txt.

# 5.Do all of the above as asynchronously and concurrently as possible. (Use aiohttp for the requests, and aiofiles for the file-appends. These are two primary examples of IO that are well-suited for the async IO model.)

The constant HREF_RE is a regular expression to extract what we’re ultimately searching for, href tags within HTML:

>>> HREF_RE.search('Go to <a href="https://realpython.com/">Real Python</a>')
<re.Match object; span=(15, 45), match='href="https://realpython.com/"'>
The coroutine fetch_html() is a wrapper around a GET request to make the request and decode the resulting page HTML. It makes the request, awaits the response, and raises right away in the case of a non-200 status:

resp = await session.request(method="GET", url=url, **kwargs)
resp.raise_for_status()
If the status is okay, fetch_html() returns the page HTML (a str). Notably, there is no exception handling done in this function. The logic is to propagate that exception to the caller and let it be handled there:

html = await resp.text()
We await session.request() and resp.text() because they’re awaitable coroutines. The request/response cycle would otherwise be the long-tailed, time-hogging portion of the application, but with async IO, fetch_html() lets the event loop work on other readily available jobs such as parsing and writing URLs that have already been fetched.

Next in the chain of coroutines comes parse(), which waits on fetch_html() for a given URL, and then extracts all of the href tags from that page’s HTML, making sure that each is valid and formatting it as an absolute path.

Admittedly, the second portion of parse() is blocking, but it consists of a quick regex match and ensuring that the links discovered are made into absolute paths.

In this specific case, this synchronous code should be quick and inconspicuous. But just remember that any line within a given coroutine will block other coroutines unless that line uses yield, await, or return. If the parsing was a more intensive process, you might want to consider running this portion in its own process with loop.run_in_executor().

Next, the coroutine write() takes a file object and a single URL, and waits on parse() to return a set of the parsed URLs, writing each to the file asynchronously along with its source URL through use of aiofiles, a package for async file IO.

Lastly, bulk_crawl_and_write() serves as the main entry point into the script’s chain of coroutines. It uses a single session, and a task is created for each URL that is ultimately read from urls.txt.

Here are a few additional points that deserve mention:

The default ClientSession has an adapter with a maximum of 100 open connections. To change that, pass an instance of asyncio.connector.TCPConnector to ClientSession. You can also specify limits on a per-host basis.

You can specify max timeouts for both the session as a whole and for individual requests.

This script also uses async with, which works with an asynchronous context manager. I haven’t devoted a whole section to this concept because the transition from synchronous to asynchronous context managers is fairly straightforward. The latter has to define .__aenter__() and .__aexit__() rather than .__exit__() and .__enter__(). As you might expect, async with can only be used inside a coroutine function declared with async def.

If you’d like to explore a bit more, the companion files for this tutorial up at GitHub have comments and docstrings attached as well.

Here’s the execution in all of its glory, as areq.py gets, parses, and saves results for 9 URLs in under a second:

tech_star01@DoHardThings01:~/Mypros/python-backend/Asynchronous-requests$ python3 areq.py
15:06:12 DEBUG:asyncio: Using selector: EpollSelector
15:06:12 ERROR:areq: aiohttp exception for https://www.politico.com/tipsheets/morning-money [403]: Forbidden
15:06:12 INFO:areq: Got response [200] for URL: https://www.ietf.org/rfc/rfc2616.txt
15:06:12 INFO:areq: Found 0 links for https://www.ietf.org/rfc/rfc2616.txt
15:06:12 INFO:areq: Got response [200] for URL: https://1.1.1.1/
15:06:12 INFO:areq: Found 36 links for https://1.1.1.1/
15:06:12 INFO:areq: Wrote results for source URL: https://1.1.1.1/
15:06:12 ERROR:areq: aiohttp exception for https://docs.python.org/3/this-url-will-404.html [404]: Not Found
15:06:13 INFO:areq: Got response [200] for URL: https://www.mediamatters.org/
15:06:13 INFO:areq: Found 86 links for https://www.mediamatters.org/
15:06:13 INFO:areq: Wrote results for source URL: https://www.mediamatters.org/
15:06:13 ERROR:areq: aiohttp exception for https://www.nytimes.com/guides/ [404]: Not Found
15:06:13 INFO:areq: Got response [200] for URL: https://regex101.com/
15:06:13 INFO:areq: Found 67 links for https://regex101.com/
15:06:13 INFO:areq: Wrote results for source URL: https://regex101.com/
15:06:13 INFO:areq: Got response [200] for URL: https://www.bloomberg.com/markets/economics
15:06:13 INFO:areq: Found 2 links for https://www.bloomberg.com/markets/economics
15:06:13 INFO:areq: Wrote results for source URL: https://www.bloomberg.com/markets/economics
