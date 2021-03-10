from typing import List, Dict
from injecta.service.Service import Service


class Tag2ServicesPreparer:
    def prepare(self, services: List[Service]) -> Dict[str, List[Service]]:
        tags2_services = {}

        for service in services:
            if not service.tags:
                continue

            for tag in service.tags:
                tag_name = tag["name"] if isinstance(tag, dict) else tag

                if tag_name not in tags2_services:
                    tags2_services[tag_name] = []

                tags2_services[tag_name].append(service)

        return tags2_services
