from pathlib import Path
from injecta.package.pathResolver import resolvePath

class ImportDefinitionResolver:

    def resolve(self, importDefinition, baseDir: Path) -> set:
        if isinstance(importDefinition, str):
            if importDefinition[0:1] == '@':
                firstSlashPosition = importDefinition.find('/')
                rootModuleName = importDefinition[1:firstSlashPosition]
                rootModulePath = resolvePath(rootModuleName)

                return {Path(rootModulePath + importDefinition[firstSlashPosition:])}

            return {baseDir.joinpath(importDefinition).resolve()}

        if isinstance(importDefinition, dict):
            if 'search' not in importDefinition:
                raise Exception('Missing the "search" main keyword in the import definition')

            if 'include' not in importDefinition['search']:
                raise Exception('Missing the "include" keyword under "search" main keyword')

            basePathGlob = set(baseDir.glob('./**/*.*'))
            allConfigsGlob = set(map(lambda path: path.resolve(), baseDir.glob(importDefinition['search']['include'])))

            return set(allConfigsGlob - basePathGlob)

        raise Exception('Unexpected import definition type: ' + type(importDefinition))
