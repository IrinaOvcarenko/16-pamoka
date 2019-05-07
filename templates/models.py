from smartninja_nosql.odm import Model

class SecretNumber(Model):
    def__init__(self, name, number, **kwargs):
    self.name = name
    self.number = number
    super().__init__(**kwargs)