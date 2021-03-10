def di_service(method):
    def wrapper(*args):
        service_name = method.__name__
        container = args[0]

        if not service_name in container.services:  # noqa: 5713
            # print('creating service ' + service_name)
            container.services[service_name] = method(*args)

        return container.services[service_name]

    return wrapper
