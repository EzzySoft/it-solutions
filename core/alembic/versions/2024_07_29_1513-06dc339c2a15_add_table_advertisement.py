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

    ads = [
        {
            "title": "Видеонаблюдение Установка Продажа Настройка Видеокамер IP",
            "author": "TVi MART",
            "views": 1488,
            "position_number": 1,
        },
        {
            "title": "Качественная установка монтаж видеонаблюдения на любой объект во Владивостоке",
            "author": "Primtec",
            "views": 317,
            "position_number": 2,
        },
        {
            "title": "ВидеоКИТ - Системы видеонаблюдения, установка, обслуживание во Владивостоке",
            "author": "VideoKIT",
            "views": 192,
            "position_number": 3,
        },
        {
            "title": "Установка камер видеонаблюдения, гарантия лучшей цены во Владивостоке",
            "author": "Vizord (Визорд)",
            "views": 523,
            "position_number": 4,
        },
        {
            "title": "Установим Видеодомофон в квартиру или частный дом! Видеонаблюдение во Владивостоке",
            "author": "Подряд",
            "views": 121,
            "position_number": 5,
        },
        {
            "title": "Установка видеонаблюдения от Vladrec | Монтаж | Обслуживание | СКУД во Владивостоке",
            "author": "VLADREC",
            "views": 203,
            "position_number": 6,
        },
    ]

    for ad in ads:
        op.execute(
            f"INSERT INTO advertisement (title, author, views, position_number) VALUES "
            f"('{ad['title']}', '{ad['author']}', {ad['views']}, {ad['position_number']})"
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
