#! /usr/bin/python
# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")


class MinimalModel(models.Model):
    _name = 'test.model'
    

class LessMinimalModel(models.Model):
    _name = 'test.model2'

    name = fields.Char(required=True)




# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

