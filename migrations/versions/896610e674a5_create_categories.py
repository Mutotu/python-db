"""create-categories

Revision ID: 896610e674a5
Revises: 198707b1bf0d
Create Date: 2022-01-04 15:20:22.949738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '896610e674a5'
down_revision = '198707b1bf0d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False, unique=True)
    )


def downgrade():
    op.drop_table('categories')
