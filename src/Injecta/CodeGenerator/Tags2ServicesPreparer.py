from typing import List
from Injecta.Service.Definition import Definition

class Tags2ServicesPreparer:

    def prepare(self, definitions: List[Definition]):
        tags2Services = {}

        for definition in definitions:
            if definition.hasTags() is False:
                continue

            for tag in definition.getTags():
                if tag not in tags2Services:
                    tags2Services[tag] = []

                tags2Services[tag].append(definition.getName())

        return tags2Services
