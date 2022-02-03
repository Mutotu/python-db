"""add_category_id_to_dinos

Revision ID: e13a94a01cdc
Revises: 896610e674a5
Create Date: 2022-01-04 15:27:18.840780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e13a94a01cdc'
down_revision = '896610e674a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('dinos', sa.Column('category_id', sa.Integer))


def downgrade():
    op.remove_column('dinos', 'category_id')
