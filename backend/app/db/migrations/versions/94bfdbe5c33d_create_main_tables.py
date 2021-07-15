"""create_main_tables
Revision ID: 94bfdbe5c33d
Revises: d12ea55c0784
Create Date: 2021-07-15 16:10:24.118616
"""

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic
revision = '94bfdbe5c33d'
down_revision = 'd12ea55c0784'
branch_labels = None
depends_on = None


def create_cleanings_table() -> None:
    op.create_table(
        "cleanings1",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )
    
def upgrade() -> None:
    create_cleanings_table()

def downgrade() -> None:
    op.drop_table("cleanings1")