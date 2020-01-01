def diService(method):
    def wrapper(*args):
        serviceName = method.__name__
        container = args[0]

        if not serviceName in container.services:
            # print('creating service ' + service_name)
            container.services[serviceName] = method(*args)

        return container.services[serviceName]

    return wrapper
