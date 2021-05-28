# run in shell
# python3 manage.py shell

from clientnav.models import usrCredentials
p = usrCredentials(u_id=0, u_name='test', u_pwd='foobar')
p.save()
from clientnav.models import mixedDrugs
p = mixedDrugs(d_id=0, d_name='popyproline')
p.save()
from clientnav.models import ingrediantList
p = ingrediantList(i_id=0, location=0, required='F')
