from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)


secrets = Table(
    "secrets",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("secret", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow()),
    Column("is_active", Boolean, default=True),
    Column("lifetime", TIMESTAMP),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("secret_id", Integer, ForeignKey("secrets.id")),
)
