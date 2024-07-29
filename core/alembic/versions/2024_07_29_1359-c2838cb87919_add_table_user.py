"""add table User

Revision ID: c2838cb87919
Revises: 
Create Date: 2024-07-29 13:59:14.166865

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c2838cb87919"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("user_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.LargeBinary(), nullable=True),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_user")),
        sa.UniqueConstraint("email", name=op.f("uq_user_email")),
        sa.UniqueConstraint("username", name=op.f("uq_user_username")),
    )
    op.create_index(op.f("ix_user_user_id"), "user", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_user_user_id"), table_name="user")
    op.drop_table("user")
