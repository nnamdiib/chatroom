create table messages (
	id integer primary key autoincrement not null,
	room text,
	username text,
	message text
);