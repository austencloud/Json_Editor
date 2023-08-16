
class SchemaRepository:
    def __init__(self):
        self.schemas = {}
        self.default_resolver = self.resolve_reference
        self.resolvers = {'default': self.default_resolver}

    def add_schema(self, name, schema):
        self.schemas[name] = schema

    def retrieve_schema(self, name):
        return self.schemas.get(name, None)

    def resolve_reference(self, ref):
        return self.schemas.get(ref, None)

    def add_resolver(self, name, resolver):
        self.resolvers[name] = resolver

    def resolve_with(self, name, ref):
        resolver = self.resolvers.get(name, self.default_resolver)
        return resolver(ref)
