from authomatic.providers import oauth2, oauth1

CONFIG = {
	'tw': {
		'class': oauth1.Twitter,
		'consumer_key': '5ROubSCwMYsCLjHd4rzlYpMjt',
		'consumer_secret': '9pyccKoHxHFG2eeVU8cFVfctYHzFqGTdvMVFQfhVVGgEFnRY52',
	},

	'fb': {
		'class': oauth2.Facebook,
		'consumer_key': '1412717765703591',
		'consumer_secret': 'fd4896a5a1d86486de69dee2a3636009',
		'scope': ['user_about_me', 'email', 'publish_stream'],
	},
}