from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.autowiring.AutowiringCompilerPass import AutowiringCompilerPass
from injecta.bundle.Bundle import Bundle
from injecta.definition.DefaultValuesSetter import DefaultValuesSetter
from injecta.definition.DefaultValuesSetterCompilerPass import DefaultValuesSetterCompilerPass
from injecta.tag.TaggedServicesCompilerPass import TaggedServicesCompilerPass

class InjectaBundle(Bundle):

    def getCompilerPasses(self):
        return [
            DefaultValuesSetterCompilerPass(DefaultValuesSetter()),
            TaggedServicesCompilerPass(),
            AutowiringCompilerPass(ArgumentsAutowirer(ArgumentResolver())),
        ]
