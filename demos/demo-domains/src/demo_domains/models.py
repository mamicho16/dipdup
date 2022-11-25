from typing import Optional

from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from dipdup.models import Model


class TLD(Model):
    id = fields.CharField(max_length=255, pk=True)
    owner = fields.CharField(max_length=36)


class Domain(Model):
    id = fields.CharField(max_length=255, pk=True)
    tld: ForeignKeyFieldInstance[TLD] = fields.ForeignKeyField('models.TLD', 'domains')
    expiry = fields.DatetimeField(null=True)
    owner = fields.CharField(max_length=36)
    token_id = fields.BigIntField(null=True)

    tld_id: Optional[str]


class Record(Model):
    id = fields.CharField(max_length=255, pk=True)
    domain: ForeignKeyFieldInstance[Domain] = fields.ForeignKeyField('models.Domain', 'records')
    address = fields.CharField(max_length=36, null=True)
