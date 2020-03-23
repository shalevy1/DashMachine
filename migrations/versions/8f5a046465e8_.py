"""empty message

Revision ID: 8f5a046465e8
Revises: 45ebff47af9f
Create Date: 2020-02-06 19:51:14.594434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8f5a046465e8"
down_revision = "45ebff47af9f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("api_calls")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "api_calls",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(), nullable=True),
        sa.Column("resource", sa.VARCHAR(), nullable=True),
        sa.Column("method", sa.VARCHAR(), nullable=True),
        sa.Column("payload", sa.VARCHAR(), nullable=True),
        sa.Column("authentication", sa.VARCHAR(), nullable=True),
        sa.Column("username", sa.VARCHAR(), nullable=True),
        sa.Column("password", sa.VARCHAR(), nullable=True),
        sa.Column("value_template", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###