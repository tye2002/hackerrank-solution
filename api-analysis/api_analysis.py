from urllib.parse import urlparse

def getResourceList(requests):
    # Function to extract resources from URLs
    def extract_resources(url):
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        resources = [part for part in path.split('/') if not part.startswith("id")]
        return resources

    # Function to sort resources by level of dependency
    def sort_resources_by_level(requests):
        resource_levels = {}
        for request in requests:
            resources = extract_resources(request)
            level = len(resources)
            if level not in resource_levels:
                resource_levels[level] = []
            resource_levels[level].append('/'.join(resources))

        # Sort resources within each level
        for level in resource_levels:
            resource_levels[level].sort()

        return resource_levels

    # Function to print resources by level of dependency
    def print_resources_by_level(resource_levels):
        result = []
        for level in sorted(resource_levels.keys()):
            result.extend(resource_levels[level])
        return result

    resource_levels = sort_resources_by_level(requests)
    return print_resources_by_level(resource_levels)

# Example usage:
requests = [
    "https://api.example.com/resource2/id/resource3/id2",
    "https://api.example.com/resource3/",
    "https://api.example.com/resource2/id",
    "https://api.example.com/resource1/id/resource3/id2"
] # result: ['resource2', 'resource3', 'resource1/resource3', 'resource2/resource3']

requests = [
    "https://api.example.com/resource915/id/resource515/",
    "https://api.example.com/resource845/",
    "https://api.example.com/resource515/id43/id43/id34/",
] # result: ['resource515', 'resource845', 'resource915/resource515']

requests = [
    "https://api.example.com/resource915/id/resource515/",
    "https://api.example.com/resource245/",
    "https://api.example.com/resource515/id43/id43/id34/",
    "https://api.example.com/resource245/resource12",
] # result: ['resource245', 'resource515', 'resource245/resource12', 'resource915/resource515']

print(getResourceList(requests))
