"""Initial migration.

Revision ID: 31cb58ff15d3
Revises: 
Create Date: 2024-06-27 21:29:18.079507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '31cb58ff15d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)

    # Check if user_account table exists before creating it
    if 'user_account' not in inspector.get_table_names():
        op.create_table('user_account',
                        sa.Column('user_id', sa.Integer(), nullable=False),
                        sa.Column('name', sa.String(
                            length=80), nullable=False),
                        sa.Column('email', sa.String(
                            length=80), nullable=False),
                        sa.Column('phone_number', sa.String(
                            length=80), nullable=True),
                        sa.Column('address', sa.String(
                            length=100), nullable=True),
                        sa.Column('password', sa.String(
                            length=40), nullable=False),
                        sa.PrimaryKeyConstraint('user_id'),
                        sa.UniqueConstraint('email')
                        )

    # Repeat similar checks for other tables
    if 'aboutus' not in inspector.get_table_names():
        op.create_table('aboutus',
                        sa.Column('content_id', sa.Integer(), nullable=False),
                        sa.Column('content_title', sa.String(
                            length=100), nullable=False),
                        sa.Column('content_text', sa.String(
                            length=500), nullable=False),
                        sa.PrimaryKeyConstraint('content_id')
                        )

    if 'car_listings' not in inspector.get_table_names():
        op.create_table('car_listings',
                        sa.Column('car_id', sa.Integer(), nullable=False),
                        sa.Column('user_id', sa.Integer(), nullable=True),
                        sa.Column('make', sa.String(
                            length=20), nullable=False),
                        sa.Column('model', sa.String(
                            length=20), nullable=False),
                        sa.Column('year', sa.Integer(), nullable=False),
                        sa.Column('mileage', sa.Integer(), nullable=False),
                        sa.Column('price', sa.Float(), nullable=False),
                        sa.Column('description', sa.String(
                            length=200), nullable=True),
                        sa.Column('image_url', sa.String(
                            length=200), nullable=False),
                        sa.ForeignKeyConstraint(
                            ['user_id'], ['user_account.user_id'], ),
                        sa.PrimaryKeyConstraint('car_id')
                        )

    if 'category' not in inspector.get_table_names():
        op.create_table('category',
                        sa.Column('cat_id', sa.Integer(), nullable=False),
                        sa.Column('category_name', sa.String(
                            length=20), nullable=False),
                        sa.PrimaryKeyConstraint('cat_id')
                        )

    if 'contactus' not in inspector.get_table_names():
        op.create_table('contactus',
                        sa.Column('contact_form_id',
                                  sa.Integer(), nullable=False),
                        sa.Column('contact_email', sa.String(
                            length=40), nullable=False),
                        sa.Column('user_id', sa.Integer(), nullable=True),
                        sa.Column('phone_number', sa.String(
                            length=20), nullable=True),
                        sa.Column('message', sa.String(
                            length=200), nullable=False),
                        sa.Column('submission_date',
                                  sa.DateTime(), nullable=False),
                        sa.ForeignKeyConstraint(
                            ['user_id'], ['user_account.user_id'], ),
                        sa.PrimaryKeyConstraint('contact_form_id')
                        )

    if 'orders' not in inspector.get_table_names():
        op.create_table('orders',
                        sa.Column('order_id', sa.Integer(), nullable=False),
                        sa.Column('user_id', sa.Integer(), nullable=True),
                        sa.Column('payment_method', sa.String(
                            length=20), nullable=False),
                        sa.Column('order_amount', sa.Float(), nullable=False),
                        sa.Column('order_date', sa.DateTime(), nullable=False),
                        sa.Column('billing_address', sa.String(
                            length=200), nullable=True),
                        sa.ForeignKeyConstraint(
                            ['user_id'], ['user_account.user_id'], ),
                        sa.PrimaryKeyConstraint('order_id')
                        )

    if 'garage' not in inspector.get_table_names():
        op.create_table('garage',
                        sa.Column('garage_id', sa.Integer(), nullable=False),
                        sa.Column('car_id', sa.Integer(), nullable=True),
                        sa.Column('user_id', sa.Integer(), nullable=True),
                        sa.ForeignKeyConstraint(
                            ['car_id'], ['car_listings.car_id'], ),
                        sa.ForeignKeyConstraint(
                            ['user_id'], ['user_account.user_id'], ),
                        sa.PrimaryKeyConstraint('garage_id')
                        )

    if 'car_listing_category' not in inspector.get_table_names():
        op.create_table('car_listing_category',
                        sa.Column('car_id', sa.Integer(), nullable=False),
                        sa.Column('cat_id', sa.Integer(), nullable=False),
                        sa.ForeignKeyConstraint(
                            ['car_id'], ['car_listings.car_id'], ),
                        sa.ForeignKeyConstraint(
                            ['cat_id'], ['category.cat_id'], ),
                        sa.PrimaryKeyConstraint('car_id', 'cat_id')
                        )


def downgrade():
    # Drop tables in reverse order if they exist
    op.drop_table('car_listing_category')
    op.drop_table('garage')
    op.drop_table('orders')
    op.drop_table('contactus')
    op.drop_table('category')
    op.drop_table('car_listings')
    op.drop_table('aboutus')
    op.drop_table('user_account')
