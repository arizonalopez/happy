from django.core.checks import Error, register, Tags

@register(Tags.compatibility)
def settings_check(app_configs, **kwargs):
    from django.conf import settings
    errors = []
    if not settings.ADMINS:
        errors.append(Error(
            'The system admins are not set in the project settings',
            hint='''in order to recieve notifications when new
videos are created, define system admins like ADMINS=(('Admin', 'admin@example.com')) in your settings''', id='misc.W001'
        ))
    return errors

