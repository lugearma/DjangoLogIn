from authomatic.providers import oauth2, oauth1

CONFIG = {
	'twitter': {
		'class_': oauth1.Twitter,
		'consumer_key': 'dtQ2TFHwuRGM2xsvMpECcyOPh',
		'consumer_secret': 'R8gNLwCnj6jL7CEoIzKls3uEU9rTAzgcH7SpkOBHyEb0ScWqgn',
	},

	'facebook': {
		'class_': oauth2.Facebook,
        'short_name': 1,
		'consumer_key': '1412717765703591',
		'consumer_secret': 'fd4896a5a1d86486de69dee2a3636009',
		'scope': ['user_about_me', 'email', 'publish_stream'],
	},
}
