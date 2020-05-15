# Using service factories

Factory service helps you with creation of other services. A typical service which should be created using factory is a **Logger** service:

```python
from logging import Logger 

class ApiClient:

    def __init__(self, logger: Logger):
        self.__logger = logger

    def get(self, path):
        self.__logger.info('Request started')

        # API request

class LoggerFactory:

    def create(self, loggerName: str):
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)    

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter('%(message)s')

        logger.handlers = [streamHandler]

        return logger
```

Associated service configuration:

```yaml
services:
    mycompany.logger.LoggerFactory:

    mycompany.api.logger:
      factory: ['@mycompany.logger.LoggerFactory', 'create']
      arguments:
        - 'my_api_logger'

    mycompany.api.ApiClient:
      arguments:
        - '@mycompany.api.logger'
```
As you can see, you can also pass arguments into factories. Such argument (`loggerName` here) might be passed into the created service then.

After defining the `LoggerFactory` service, you may use it to create as many loggers as needed.
