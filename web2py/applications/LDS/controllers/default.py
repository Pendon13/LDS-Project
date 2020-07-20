# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
import case
import elements

def index():

    if request.vars.formulaInput:
        session.formulaInput = request.vars.formulaInput
        initialFormula = session.formulaInput
        session.convertedFormula = case.convertFormula(request.vars.formulaInput)
        session.formulaDB = session.formulaInput.replace("^","")
        session.case = case.choosingCase(request.vars.formulaInput, session.convertedFormula)
        session.htmlFormula = case.generateHTMLFormula(session.convertedFormula)
        ###########
        # Case 1a #
        ###########
        session.lonePairCase1a = case.lonePairCase1a(session.convertedFormula)
        session.doubleBondCase1a = case.doubleBondCase1a(session.convertedFormula)
        session.numBondCase1a = case.numBondCase1a(session.convertedFormula, session.doubleBondCase1a)
        ###########
        # Case 1b #
        ###########
        session.lonePairCase1b = case.lonePairCase1b(session.convertedFormula)
        session.numBondCase1b = case.numBondCase1b(session.convertedFormula)
        session.ringsCase1b = case.ringsCase1b(session.convertedFormula)
        ###########
        # Case 2a #
        ###########
        session.lonePairCase2a = case.lonePairCase2a(session.convertedFormula)
        session.doubleBondCase2a = case.doubleBondCase2a(session.convertedFormula)
        session.numBondCase2a = case.numBondCase2a(session.convertedFormula, session.doubleBondCase2a)
        ###########
        # Case 2b #
        ###########
        session.lonePairCase2b = case.lonePairCase2b(session.convertedFormula)
        session.doubleBondCase2b = case.doubleBondCase2b(session.convertedFormula)
        session.numBondCase2b = case.numBondCase2b(session.convertedFormula, session.doubleBondCase2b)
        ###########
        # Case 3a #
        ###########
        session.lonePairCase3a = case.lonePairCase3a(session.convertedFormula)
        session.doubleBondCase3a = case.doubleBondCase3a(session.convertedFormula)
        session.numBondCase3a = case.numBondCase3a(session.convertedFormula, session.doubleBondCase3a)
        ###########
        # Case 3b #
        ###########
        session.lonePairCase3b = case.lonePairCase3b(session.convertedFormula)
        session.doubleBondCase3b = case.doubleBondCase3b(session.convertedFormula)
        session.numBondCase3b = case.numBondCase3b(session.convertedFormula, session.doubleBondCase3b)
        redirect(URL('second'))
    return dict()

def second():
    return dict(message=T('success'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
