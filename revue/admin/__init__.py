from flask_nav.elements import View, Subgroup

from revue import nav
from revue.utilities.ui.bootstrap import CustomNavbar

admin_navbar = CustomNavbar(
    'Revue',
    [
        View('Home', '.index'),
        View('Activations', '.registrations'),
        View('Users', '.all_users'),
        Subgroup('Groups',
                 View('All groups', '.group_page'),
                 View('Years', '.show_all_years')
                 ),
        Subgroup('Mail',
                 View('Lists', '.view_mailing_lists'),
                 View('Update files', '.generate_mail_lists')
                 )
    ], [
        Subgroup('Admin',
                 View('Public', 'public.index'),
                 View('Intern', 'intern.index'),
                 ),
        Subgroup('Account',
                 View('Profiel', 'intern.profile'),
                 View('Groups', 'intern.view_own_groups'),
                 View('Logout', 'intern.logout'),
                 ),
    ]
)
nav.register_element('admin_navbar', admin_navbar)
