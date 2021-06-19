from schematics.exceptions import ValidationError
from schematics.types import BaseType
import re


class ISO_4217(BaseType):
    def validate_ISO(self, value):
        if not bool(re.match(r'[A-Z]{3}', value)):
            raise ValidationError('No sigue la norma ISO')