class ServiceMethodNameTranslator:

    def translate(self, dtypeStr: str):
        return '__' + dtypeStr.replace('.', '_')
