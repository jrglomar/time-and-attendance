"""create initial database tables

Revision ID: e3d4877abf03
Revises: 
Create Date: 2021-08-14 15:37:21.883072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d4877abf03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_types',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'employee_types',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'users',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('user_type_id', sa.String(36), sa.ForeignKey('user_types.id'), nullable=True),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('password', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'shift_types',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('start_time', sa.Time, nullable=True),
        sa.Column('end_time', sa.Time, nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'employees',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('employee_type_id', sa.String(36), sa.ForeignKey('employee_types.id'), nullable=True),
        sa.Column('user_id', sa.String(36), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('shift_type_id', sa.String(36), sa.ForeignKey('shift_types.id'), nullable=True),
        sa.Column('monday', sa.String(255), nullable=True),
        sa.Column('tuesday', sa.String(255), nullable=True),
        sa.Column('wednesday', sa.String(255), nullable=True),
        sa.Column('thursday', sa.String(255), nullable=True),
        sa.Column('friday', sa.String(255), nullable=True),
        sa.Column('saturday', sa.String(255), nullable=True),
        sa.Column('sunday', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'time_ins',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('employee_id', sa.String(36), sa.ForeignKey('employees.id'), nullable=True),
        sa.Column('time_log', sa.Time, nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'time_outs',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('employee_id', sa.String(36), sa.ForeignKey('employees.id'), nullable=True),
        sa.Column('time_log', sa.Time, nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'attendances',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('employee_id', sa.String(36), sa.ForeignKey('employees.id'), nullable=True),
        sa.Column('time_in_id', sa.String(36), sa.ForeignKey('time_ins.id'), nullable=True),
        sa.Column('time_out_id', sa.String(36), sa.ForeignKey('time_outs.id'), nullable=True),
        sa.Column('hours_worked', sa.Integer, nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'leave_types',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.Date, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.Date, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'leave_sub_types',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('leave_type_id', sa.String(36), sa.ForeignKey('leave_types.id'), nullable=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    op.create_table(
        'leaves',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('employee_id', sa.String(36), sa.ForeignKey('employees.id'), nullable=True),
        sa.Column('leave_type_id', sa.String(36), sa.ForeignKey('leave_types.id'), nullable=True),
        sa.Column('leave_sub_type_id', sa.String(36), sa.ForeignKey('leave_sub_types.id'), nullable=True),
        sa.Column('title', sa.String(255), nullable=True),
        sa.Column('status', sa.String(255), nullable=True, server_default=sa.text("'Pending'")),
        sa.Column('reason', sa.String(500), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('active_status', sa.String(255), nullable=True, server_default=sa.text("'Active'")),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_onupdate=sa.text('NOW()'))
    )
    
    


def downgrade():
    pass
