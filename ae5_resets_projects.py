import os

#get active sessions
def active_deployments():
    active_sessions="kubectl get deploy | grep session | cut -d' ' -f1"
    session=os.popen(active_sessions).read()
    sessions_list = session.split("\n")
    new_list = []
    for each in sessions_list:
        s_id=('a1-'+each.strip('anaconda-session-'))
        new_list.append(s_id)

    new_list = filter(None, new_list)
    return list(new_list)

#get DB sessions
def db_sessions():
    db_sessions="ae5 session list --columns=id --no-header"
    session=os.popen(db_sessions).read()
    db_sessions_list = session.split("\n")
    db_sessions_list = filter(None, db_sessions_list)

    return list(db_sessions_list)

#find db sessions with no matching deployment and delete it
def delete_session(new_list, db_sessions_list):
    stop="ae5 session stop"
    for session in db_sessions_list:
        if session not in new_list:
            os.system(stop + ' ' + session + ' ' + '--yes')
        else:
            pass

new_list=active_deployments()
db_sessions_list=db_sessions()
delete_session(new_list, db_sessions_list)
