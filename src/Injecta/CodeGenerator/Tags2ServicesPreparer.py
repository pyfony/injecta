class Tags2ServicesPreparer:
    
    def prepare(self, definitions: list):
        tags2Services = {}

        for definition in definitions:
            if definition.hasTags() == False:
                continue

            for tag in definition.getTags():
                if tag not in tags2Services:
                    tags2Services[tag] = []

                tags2Services[tag].append(definition.getName())

        return tags2Services
