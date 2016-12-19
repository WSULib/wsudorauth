from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


def index(request):

    return JsonResponse({
			'name':'wsudorauth',
			'info':'https://github.com/WSULib/wsudorauth'
		}, status=200)


def whoami(request):

	return JsonResponse({
		'username':request.user.username,
		'first_name':request.user.first_name,
		'last_name':request.user.last_name,
		'session_id':request.session.session_key,
		'session_check': '%s/session_check/%s' % (request.build_absolute_uri().split('/whoami')[0], request.session.session_key)
	})


def session_check(request, session_id=False):

	'''
	Given a sessionid, return user credentials
	re: http://scottbarnham.com/blog/2008/12/04/get-user-from-session-key-in-django/
	'''

	if session_id:

		print "checking session_id: %s" % session_id

		try:
			session = Session.objects.get(session_key=session_id)
		except:
			session = False

		if session:

			uid = session.get_decoded().get('_auth_user_id')
			user = User.objects.get(pk=uid)

			return JsonResponse({
				'username':user.username,
				'first_name':user.first_name,
				'last_name':user.last_name
			})

		else:
			return JsonResponse({
				'status':'false',
				'message':'session id not found in active sessions',
				'session_id': session_id
			}, status=404)


	else:
		return JsonResponse({
			'status':'false',
			'message':'session id not provided'
		}, status=400)

