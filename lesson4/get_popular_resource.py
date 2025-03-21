import re


def get_popular_resource(filename):
    with open(filename, 'r') as file:
        resources = dict()
        match = re.compile(r'https?://[^/]+(/[^\s"]+)')
        line = file.readline()
        while line:
            resource_match = match.search(line)
            if resource_match:
                resource = resource_match.group(1)
                if resource in resources:
                    resources[resource] += 1
                else:
                    resources.setdefault(resource, 0)
            line = file.readline()

        resources = sorted(resources.items(), key=lambda item: item[1],
                           reverse=True)
        if len(resources) > 0:
            return resources[0]
        return None
