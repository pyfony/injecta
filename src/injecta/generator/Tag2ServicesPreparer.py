from typing import List, Dict
from injecta.service.Service import Service

class Tag2ServicesPreparer:

    def prepare(self, services: List[Service]) -> Dict[str, List[Service]]:
        tags2Services = {}

        for service in services:
            if not service.tags:
                continue

            for tag in service.tags:
                tagName = tag['name'] if isinstance(tag, dict) else tag

                if tagName not in tags2Services:
                    tags2Services[tagName] = []

                tags2Services[tagName].append(service)

        return tags2Services
