#!/usr/bin/env python

from distutils.core import setup
import stalwart
setup(
	name='stalwart',
	version=stalwart.__version__,
	description='Stalwart plugins',
	author='Mitko Masarliev',
	author_email='mitko@masalriev.net',
	url='http://masarliev.net/',
	packages=['stalwart', 'stalwart.piecemaker', 'stalwart.livelog'],
	package_data={
		'stalwart': [
			'livelog/media/livelog/images/*.png',
			'livelog/media/livelog/style/*.css',
			'livelog/media/livelog/js/*.js',
			'livelog/templates/admin/*.html',
			'piecemaker/media/piecemaker/*.css',			
			'piecemaker/media/piecemaker/*.sfw',
			'piecemaker/media/piecemaker/scripts/swfobject/*.js',		
			'piecemaker/media/piecemaker/scripts/swfobject/*.swf',
			'piecemaker/templates/piecemaker/cms/*.html',
			'piecemaker/templates/piecemaker/cms/*.xml'		
			]
	}
)