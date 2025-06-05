import logging

from datetime import datetime

import sqlalchemy as sa

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship





logger = logging.getLogger(__name__)


class AuditMixin(object):
    """
    AuditMixin
    Mixin for models, adds 4 columns to stamp,
    time and user on creation and modification
    will create the following columns:

    :created on:
    :changed on:
    :created by:
    :changed by:
    """

    created_on = Column(DateTime, default=lambda: datetime.now(), nullable=False)
    changed_on = Column(
        DateTime,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now(),
        nullable=False,
    )

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "User",
            primaryjoin="%s.created_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def changed_by_fk(cls):
        return Column(
            Integer,
            ForeignKey("ab_user.id"),
            default=cls.get_user_id,
            onupdate=cls.get_user_id,
            nullable=False,
        )

    @declared_attr
    def changed_by(cls):
        return relationship(
            "User",
            primaryjoin="%s.changed_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )


class AuditMixinNullable(AuditMixin):
    """Altering the AuditMixin to use nullable fields

    Allows creating objects programmatically outside of CRUD
    """

    created_on = sa.Column(sa.DateTime, default=datetime.now, nullable=True)
    changed_on = sa.Column(
        sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=True
    )


    @declared_attr
    def created_by(cls):
        return relationship(
            "UserV2",
            primaryjoin="%s.created_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def changed_by(cls):
        return relationship(
            "UserV2",
            primaryjoin="%s.changed_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )


