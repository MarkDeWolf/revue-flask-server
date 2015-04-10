__author__ = 'fkint'


from ...models import YearGroupParticipation, Page, PageAccessRestriction
from ..session import *

def user_meets_restriction(restriction, user_id):
    ygp = YearGroupParticipation.query.filter_by(year_group=restriction.year_group, year=restriction.revue_year, user=user_id).first()
    if ygp is None:
        return False
    return True


def has_access_to_page(page, user_id):
    if not page.access_restricted:
        return True
    restrictions = PageAccessRestriction.query.filter_by(page=page.id).all()
    for restriction in restrictions:
        if user_meets_restriction(restriction, user_id):
            return True
    return False


def get_page(path):
    path_parts = path.split("/")
    current_page = None
    for p in path_parts:
        if p == "":
            continue
        parent_page_id = None
        if current_page is not None:
            parent_page_id = current_page.id
        current_page = Page.query.filter_by(url_identifier=p,parent_page=parent_page_id).first()
        if current_page is None:
            return None
    if has_access_to_page(current_page, session.get_current_user_id()):
        return current_page
    return None
