# Service Autowiring

Injecta uses autowiring-by-type for constructor/__init__() dependencies only.

## Autowiring by explicit type

```python
from mycompany.authenticator.RestAuthenticator import RestAuthenticator 

class ApiClient:

    def __init__(self, authenticator: RestAuthenticator):
        self.__authenticator = authenticator

    def get(self, path):
        token = self.__authenticator.authenticate()

        # API request

class RestAuthenticator:

    def authenticate(self):
        # authentication logic
```

Without autowiring, you would need to define the services explicitly with all arguments:

```yaml
services:
    mycompany.api.ApiClient:
      arguments:
        - '@mycompany.authenticator.RestAuthenticator'

    mycompany.authenticator.RestAuthenticator:
```

When using autowiring, the `mycompany.api.ApiClient` first argument may be omitted from the configuration. Injecta will wire it automatically based on the argument type defined in the `ApiClient` class' constructor.   

```yaml
services:
    mycompany.api.ApiClient:

    mycompany.authenticator.RestAuthenticator:
```

## Autowiring by interface

Autowiring works the same way for interfaces, however each interface must have exactly one implementation. If you create services based on multiple classes implementing the same interface, autowiring will fail and you would need to wire the services manually.   

```python

from mycompany.authenticator.AuthenticatorInterface import AuthenticatorInterface 

class ApiClient:

    def __init__(self, authenticator: AuthenticatorInterface):
        self.__authenticator = authenticator

    def get(self, path):
        token = self.__authenticator.authenticate()

        # API request

class RestAuthenticator(AuthenticatorInterface):

    def authenticate(self):
        # authentication logic
```

The service configuration remains the same:

```yaml
services:
    mycompany.api.ApiClient:

    mycompany.authenticator.RestAuthenticator:
```

## Disabling autowing

For some services, it might be necessary to disable autowiring completely. If so, the service must be wired manually:

```yaml
services:
    mycompany.api.ApiClient:
      arguments:
        - '@mycompany.authenticator.RestAuthenticator'

    mycompany.authenticator.RestAuthenticator:
      autowire: False
```
