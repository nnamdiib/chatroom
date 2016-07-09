import os
import uuid
import json
import tornado.ioloop
import tornado.web
from tornado import websocket


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/test.html")


def main():
	settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"cookie_secret": 'rrf',

	}
	app = tornado.web.Application([
		(r"/", MainHandler),
		(r"/static/", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
		], **settings)

	app.listen(8888)
	print 'Hello world app started'
	print 'listening on 8888'
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()