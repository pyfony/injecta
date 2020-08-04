from pathlib import Path
from injecta.package.pathResolver import resolvePath

def resolveRealResourcePath(packageResourcePath: str) -> Path:
    if packageResourcePath[0:1] != '@':
        raise Exception('Package resource path must start with @[packageName]')

    firstSlashPosition = packageResourcePath.find('/')
    rootModuleName = packageResourcePath[1:firstSlashPosition]
    rootModulePath = resolvePath(rootModuleName)

    return Path(rootModulePath + packageResourcePath[firstSlashPosition:])
