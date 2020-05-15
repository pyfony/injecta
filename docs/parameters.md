# Configuring services using parameters

In a real-world app, most services requires some configuration using input values:

```yaml
services:
    mycompany.api.Authenticator:
      arguments:
        - 'https://api.mycompany.com'
        - 'd1a654fe84fgs65g4sedf4s6e5f' # token
```

Converting such input values into parameters makes them **reusable for multiple services**. Parameters are constants (string, int, bool, dict, ...) to be used to configure your services in a reusable way.

```yaml
parameters:
  api:
    endpoint: 'https://api.mycompany.com'
    token: 'd1a654fe84fgs65g4sedf4s6e5f'

services:
    mycompany.api.Authenticator:
      arguments:
        - '%api.endpoint%'
        - '%api.token%'
```

Multiple parameters can be also combined into a single value:

```yaml
parameters:
  company:
    domain: mycompany.com

  api:
    endpoint: 'https://api.%company.domain%'
    token: 'd1a654fe84fgs65g4sedf4s6e5f'

services:
    mycompany.api.Authenticator:
      arguments:
        - '%api.endpoint%'
        - '%api.token%'
```

Storing token into the yaml configuration does not seem like the most secure solution. Let's use environment variables instead:

```yaml
parameters:
  company:
    domain: mycompany.com

  api:
    endpoint: 'https://api.%company.domain%'

services:
    mycompany.api.Authenticator:
      arguments:
        - '%api.endpoint%'
        - '%env(API_TOKEN)%'
```

## Named arguments

Contructor arguments can be also specified using their names: 

```yaml
services:
    mycompany.api.Authenticator:
      arguments:
        baseUrl: 'https://api.mycompany.com'
        token: 'd1a654fe84fgs65g4sedf4s6e5f'
```

Always use either argument list or named arguments. Those approaches **cannot be combined due to the limitation of the YAML syntax**.
