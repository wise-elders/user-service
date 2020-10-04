from schematics.models import Model
from schematics.types import StringType


class User(Model):
    username = StringType()
