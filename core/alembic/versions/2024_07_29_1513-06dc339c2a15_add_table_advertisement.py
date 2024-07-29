"""add table advertisement

Revision ID: 06dc339c2a15
Revises: c2838cb87919
Create Date: 2024-07-29 15:13:11.570122

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "06dc339c2a15"
down_revision: Union[str, None] = "c2838cb87919"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "advertisement",
        sa.Column("ad_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("author", sa.String(), nullable=False),
        sa.Column("views", sa.Integer(), nullable=False),
        sa.Column("position_number", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("ad_id", name=op.f("pk_advertisement")),
    )
    op.create_index(
        op.f("ix_advertisement_ad_id"),
        "advertisement",
        ["ad_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_advertisement_ad_id"), table_name="advertisement")
    op.drop_table("advertisement")
