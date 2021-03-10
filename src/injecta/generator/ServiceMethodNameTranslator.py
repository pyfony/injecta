class ServiceMethodNameTranslator:
    def translate(self, dtype_str: str):
        return "__" + dtype_str.replace(".", "_")
