import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

const db = await open({
	filename: './mydb.sqlite',
	driver: sqlite3.Database
});
