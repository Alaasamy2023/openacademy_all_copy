# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
from datetime import timedelta

class Course (models.Model):
    _name = 'openacademy.course'
    _inherit = 'mail.thread'
    _description = 'OpenAcademy Course'

    name = fields.Char(string="title",required=True,tracking=True)
    description = fields.Text(tracking=True)
    responsible_id=fields.Many2one("res.users",Ondelete="set null",string="Responsible",Index=True,tracking=True)
    # session_id=fields.One2many("openacademy.session","course_id",string="Sessions",tracking=True)

    state = fields.Selection(
        [
            ('draft', "Draft"),
            ('submitted', "Submitted"),
            ('department_manager_approved', "Department Manager Approved"),
            ('college_manager', "College Manager Approved"),
            ('disapproved', "Disapproved"),('finally_approved', "Finally_approved")
        ],string="Course Status",readonly=True, copy=False,default='draft',tracking=True)











    def submitted_action(self):
        for rec in self:
            rec.state='submitted'

    def department_manager(self):
        for rec in self:
            rec.state='department_manager_approved'


    def disapproved_action(self):
        for rec in self:
            rec.state='disapproved'

    def finally_approved_action(self):
        for rec in self:
            rec.state='finally_approved'

    def college_manager(self):
        for rec in self:
            rec.state='college_manager'


    def reset_to_draft(self):
        for rec in self:
            rec.state='draft'

    _sql_constraints = [
        ('name_description_check', 'CHECK(name!= description)', "the title of course should not be the title of description"),

        ('name_uniq', 'unique (name)', "Tag name already exists !")
    ]
