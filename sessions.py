''' Generate session for valid login '''
def createSession(ip, u, p): ''' 2 unknown pieces of information added such as IP and password '''
    cst = digits
    rd = ''.join(random.choice(cst) for i in range(4))
    sk = md5(str.encode(ip) + str.encode(u) + str.encode(p) + str.encode(rd)).hexdigest()
    with open('./app/admin_session', mode='w') as session_file:
        session_file.write(sk)
    
    return sk

''' Validate already logged in user '''
def validateLoginSession():
    if 'REALSESSION' in request.cookies: ''' Does a cookie named REALSESSION already exist? '''
        activeSession = request.cookies.get('REALSESSION') 
        if database.check_login_by_session(activeSession): ''' Check against the database for logged in admin session '''
            return activeSession ''' Success '''
        else:
            return False ''' Failed session validation '''
    else:
        return False ''' Failed session validation '''

''' If use is already logged in and trying to access /login then redirect them to /index '''
