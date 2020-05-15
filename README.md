# Injecta

Dependency Injection (DI) Container written in Python. Main component of the [Pyfony Framework](https://github.com/pyfony/pyfony).

## Installation

```
$ pip install injecta
```

## Simple container initialization

(The following steps are covered in the [ContainerInitializerTest](src/injecta/container/ContainerInitializerTest.py))

To start using Injecta, create a simple `config.yaml` file to define your DI services:

```yaml
parameters:
  api:
    endpoint: 'https://api.mycompany.com'

services:
    mycompany.api.ApiClient:
      arguments:
        - '@mycompany.api.Authenticator'

    mycompany.api.Authenticator:
      class: mycompany.authenticator.RestAuthenticator
      arguments:
        - '%api.endpoint%'
        - '%env(API_TOKEN)%'
```

Then, initialize the container:

```python
from injecta.container.ContainerBuilder import ContainerBuilder
from injecta.config.YamlConfigReader import YamlConfigReader
from injecta.container.ContainerInitializer import ContainerInitializer

config = YamlConfigReader().read('/path/to/config.yaml')

containerBuild = ContainerBuilder().build(config)

container = ContainerInitializer().init(containerBuild)
```

Use `container.get()` to finally retrieve your service:

```python
from mycompany.api.ApiClient import ApiClient

apiClient = container.get('mycompany.api.ApiClient') # type: ApiClient   
apiClient.get('/foo/bar')
```

## Advanced examples

1. [Configuring services using parameters](docs/parameters.md)
1. [Service autowiring](docs/autowiring.md)
1. [Using service factories](docs/factories.md)
1. [Tagged services](docs/tagging.md)
