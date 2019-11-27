import os

try:
	SECRET_KEY = os.environ['SECRET_KEY']
except KeyError as e:
	raise EnvironmentError('SECRET_KEY environment variable needs to be set in production', e)
# just in case
Debug = False
