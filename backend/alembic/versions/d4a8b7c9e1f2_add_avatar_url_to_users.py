"""add avatar_url to users table

Revision ID: d4a8b7c9e1f2
Revises: 8c41d7e2a5f3
Create Date: 2026-09-28 15:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4a8b7c9e1f2'
down_revision: Union[str, Sequence[str], None] = '8c41d7e2a5f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _has_column(table: str, column: str) -> bool:
    inspector = sa.inspect(op.get_bind())
    if not inspector.has_table(table):
        return False
    return column in {c["name"] for c in inspector.get_columns(table)}


def upgrade() -> None:
    if not _has_column("users", "avatar_url"):
        op.add_column(
            "users",
            sa.Column("avatar_url", sa.String(length=2048), nullable=True),
        )


def downgrade() -> None:
    if _has_column("users", "avatar_url"):
        op.drop_column("users", "avatar_url")
