"""create-dinos

Revision ID: 198707b1bf0d
Revises: 
Create Date: 2022-01-04 11:29:47.439655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198707b1bf0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dinos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False, unique=True),
        sa.Column('type', sa.String, )
    )


def downgrade():
    op.drop_table('dinos')
