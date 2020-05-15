# Tagged services

Services created by Injecta can be tagged to simplify autowiring of the same-type services. This approach is especially useful when creating reusable [Pyfony Framework](https://github.com/pyfony/pyfony) bundles (packages)

```python
from typing import List

class ListClientsCommand(CommandInterface):
    
    def printList(self):
        pass

class ListProductsCommand(CommandInterface):
    
    def printList(self):
        pass

class ListInvoicesCommand(CommandInterface):
    
    def printList(self):
        pass

class ListingCommandsManager:

    def __init__(self, commands: List[CommandInterface]):
        self.__commands = commands

    def printList(self):
        for command in self.__commands:
            command.printList()
```

Each command service is tagged with the `list_command` tag. By using the `!tagged list_command` we inject all command services into the `ListingCommandsManager`.

```yaml
services:
    mycompany.client.ListClientsCommand:
      tags:
        - 'list_command'

    mycompany.product.ListProductsCommand:
      tags:
        - 'list_command'

    mycompany.invoice.ListInvoicesCommand:
      tags:
        - 'list_command'

    mycompany.commands.ListingCommandsManager:
      arguments:
        - !tagged list_command
```

For a **more real world example of useful service tagging**, see the [console-bundle configuration](https://github.com/pyfony/console-bundle/blob/master/src/consolebundle/_config/config.yaml).
