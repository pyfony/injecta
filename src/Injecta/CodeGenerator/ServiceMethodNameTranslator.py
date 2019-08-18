class ServiceMethodNameTranslator:

    def translate(self, classFqn: str):
        return '__' + classFqn[0].upper() + classFqn[1:].replace('.', '_')
