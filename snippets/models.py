"""
models.py file
"""
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True,db_column='sn_created')
    title = models.CharField(max_length=100, blank=True, default='',db_column='sn_title')
    code = models.TextField(db_column='sn_code')
    linenos = models.BooleanField(default=False,db_column='sn_linenos')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python',
    max_length=100,db_column='sn_language')
    style = models.CharField(choices=STYLE_CHOICES,default='friendly',
    max_length=100, db_column='sn_style')
    owner = models.ForeignKey('auth.User', related_name='snippets',
    on_delete=models.CASCADE, db_column='sn_owner')
    highlighted = models.TextField(db_column='sn_highlighted')

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        db_table = 'CM_Snippet_tbl'
        ordering = ['created']





class MailingListHRDatabaseUsers(models.Model):
    cuid = models.CharField(max_length=11, db_column='CG_ML_HR_OBS_CUID')
    source = models.CharField(max_length=4, db_column='CG_ML_HR_OBS_SOURCE', null=True)
    location = models.CharField(max_length=10, db_column='CM_STP_LOCATION_ID')
    department = models.CharField(max_length=10, db_column='CM_STP_DEPTID')
    reg_temp = models.CharField(max_length=30, db_column='CG_ML_HR_OBS_REGTMP', null=True)
    empl_status = models.CharField(max_length=1, db_column='CG_ML_HR_OBS_EMPLSTATUS', null=True)
    empl_description = models.CharField(max_length=50, db_column='CG_ML_HR_OBS_EMPLSTATUS_DESC', null=True)
    empl_class = models.CharField(max_length=10, db_column='CG_ML_HR_OBS_EMPL_CLASS')
    first_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_FIRST_NM', null=True)
    pref_first_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_PREF_FIRST_NM', null=True)
    middle_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_MIDDLE_NM', null=True)
    last_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_LAST_NM', null=True)
    pref_last_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_PREF_LAST_NM', null=True)
    prefix = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_PREFIX', null=True)
    email = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_EMAIL', null=True)
    is_supervisor_mngr = models.BooleanField(default=False, db_column='CG_ML_HR_OBS_IS_SUP_MGR')
    is_functional_mngr = models.BooleanField(default=False, db_column='CG_ML_HR_OBS_IS_FUNC_MGR')
    refresh_date_time = models.DateTimeField(db_column='CG_ENTRY_CREATION_DATE_TIME', auto_now_add=True)
    legal_type = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_LEGAL_TYPE', null=True)
    eq_leg_entity_desc = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_EQ_LEG_ENTITY_DESC', null=True)
    eq_rcv_comm_flag = models.BooleanField(default=False, db_column='CG_ML_HR_OBS_EQ_RCV_COMM_FLG')
    hr_flag = models.CharField(max_length=15, db_column='CG_ML_HR_OBS_FLAG', blank=True, default='', null=True)
    ofcr_code = models.CharField(max_length=2, db_column='CG_ML_HR_OBS_OFCR_CD', blank=True, default='')
    company_id = models.CharField(max_length=50, db_column='CG_ML_HR_OBS_COMPANY_ID', blank=True, default='')
    company_desc = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_COMPANY_desc', blank=True, default='')
    location_desc = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_LOCATION_DESCR', blank=True, default='')
    emptype_desc = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_EMPL_TYPE_DESCR', blank=True, default='')
    country = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_COUNTRY', blank=True, default='')
    region = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_REGION', blank=True, default='')
    descr200 = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_DESCR200', blank=True, default='')
    descr2000 = models.CharField(max_length=2000, db_column='CG_ML_HR_OBS_DESCR2000', blank=True, default='')
    dept_name = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_DEPTNAME', blank=True, default='')
    city = models.CharField(max_length=255, db_column='CG_ML_HR_OBS_CITY', blank=True, default='')
    supervisor_mngr_cuid = models.CharField(max_length=255, db_column='CG_ML_HR_SUP_MGR_CUID', blank=True, default='')
    supervisor_mngr_email = models.CharField(max_length=255, db_column='CG_ML_HR_SUP_MGR_EMAIL', blank=True, default='')
    functional_mngr_cuid = models.CharField(max_length=255, db_column='CG_ML_HR_FUNC_MGR_CUID', blank=True, default='')
    functional_mngr_email = models.CharField(max_length=255, db_column='CG_ML_HR_FUNC_MGR_EMAIL', blank=True, default='')
    per_org = models.CharField(max_length=255, db_column='CG_ML_HR_PER_ORG', blank=True, default='')
    termination_date = models.DateField(db_column='CG_ML_HR_TERMINATION_DATE', null=True)
    contract_end_date = models.DateField(db_column='CG_ML_HR_CONTRACT_END_DATE', null=True)

    class Meta:
        db_table = 'CM_Mailing_list_HR_DB_Users_tbl'
