**Company: ShopBack**
# Requirements:
There are several interdependent resources being served from `"https://api.example.com"` where each resource is parameterized with some id. For example, the API `"https://api.example.com/resource1/id1/resource2/id2/resource3/id3"` serves the resource `"resource1/resource2/resource3"` and is said to have a 3-level dependency. 

Given *n* strings as an array, requests, list the resources served with single-level dependency, followed by two-level dependency, followed by 3-level dependency, and so on. Each level of resources should be in lexicographically sorted order, e.g. resource1 precedes resource 10 which precedes resource2. 

Note: Each of the served resources has the form "resource/id". 

Example: Suppose *n = 4* and requests = 
`["https://api.example.com/resource2/id/resource3/id2", "https://api.example.com/resource3/", "https://api.example.com/resource2/id", "https://api.example.com/resource1/id/resource3/id2"]`

Expected Output:
`['resource2', 'resource3', 'resource1/resource3', 'resource2/resource3']`