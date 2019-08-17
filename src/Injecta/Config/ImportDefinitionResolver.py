from pathlib import Path

class ImportDefinitionResolver:

    def resolve(self, importDefinition, baseDir: Path) -> set:
        if isinstance(importDefinition, str):
            return {baseDir.joinpath(importDefinition).resolve()}
        elif isinstance(importDefinition, dict):
            if 'search' not in importDefinition:
                raise Exception('Missing the "search" main keyword in the import definition')

            if 'include' not in importDefinition['search']:
                raise Exception('Missing the "include" keyword under "search" main keyword')

            basePathGlob = set(baseDir.glob('*.*'))
            allConfigsGlob = set(map(lambda path: path.resolve(), baseDir.glob(importDefinition['search']['include'])))

            return set(allConfigsGlob - basePathGlob)
