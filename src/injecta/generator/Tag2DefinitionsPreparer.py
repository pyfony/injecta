from typing import List, Dict
from injecta.definition.Definition import Definition

class Tag2DefinitionsPreparer:

    def prepare(self, definitions: List[Definition]) -> Dict[str, List[Definition]]:
        tags2Services = {}

        for definition in definitions:
            if not definition.tags:
                continue

            for tag in definition.tags:
                tagName = tag['name'] if isinstance(tag, dict) else tag

                if tagName not in tags2Services:
                    tags2Services[tagName] = []

                tags2Services[tagName].append(definition)

        return tags2Services
