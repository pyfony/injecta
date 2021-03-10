import inspect
from injecta.container.ContainerInterface import ContainerInterface


def test_services(container: ContainerInterface):
    service_names = get_service_names(container)

    for service_name in service_names:
        container.get(service_name)


def get_service_names(container: ContainerInterface):
    def services_only(method_name: str, container: ContainerInterface):
        return method_name[0:12] == "_Container__" and inspect.ismethod(getattr(container, method_name))

    container_methods = list(filter(lambda method_name: services_only(method_name, container), dir(container)))

    def method_name_2_service_name(method_name: str):
        return method_name[12:].replace("_", ".")

    return list(map(method_name_2_service_name, container_methods))
