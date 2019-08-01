from injazati import error_conf



def check_for_registration_data(data):

    if not data.get('email'):
        return error_conf.EMAIL_NOT_PROVIDED

    if not data.get('password'):
        return error_conf.PASSWORD_NOT_PROVIDED


