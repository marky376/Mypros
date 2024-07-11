# In this section, i’ll build a web-scraping URL collector, areq.py, using aiohttp, a blazingly fast async HTTP client/server framework. (I just need the client part.) Such a tool could be used to map connections between a cluster of sites, with the links forming a directed graph.

# The high-level program structure will look like this:

# 1.Read a sequence of URLs from a local file, urls.txt.

# 2.Send GET requests for the URLs and decode the resulting content. If this fails, stop there for a URL.

# 3.Search for the URLs within href tags in the HTML of the responses.

# 4.Write the results to foundurls.txt.

# 5.Do all of the above as asynchronously and concurrently as possible. (Use aiohttp for the requests, and aiofiles for the file-appends. These are two primary examples of IO that are well-suited for the async IO model.)
