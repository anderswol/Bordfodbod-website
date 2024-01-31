import sqlite3 from 'sqlite3';
import { open } from 'sqlite';
import { json } from '@sveltejs/kit';

const db = await open({
	filename: './bordfodbold.db',
	driver: sqlite3.Database
});

async function initialise_db(db: Database) {
	await db.exec(`
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    `);
}

class BordfodboldController {
	constructor(private db: Database) {
		initialise_db(db);
	}

	async getPlayers() {
		return await db.all('SELECT * FROM player');
	}

	async addPlayer(name: string) {
		const stmt = await db.prepare('INSERT INTO player (name) VALUES (?)');
		await stmt.run(name);
		await stmt.finalize();
	}
}

const controller = new BordfodboldController(db);

export async function GET({}) {
	return json(await controller.getPlayers());
}

export async function POST({ request }) {
	const body = await request.json();
	// try to add the player, if they exist, we get an error
	try {
		await controller.addPlayer(body.name);
	} catch (err) {
		return json({ error: err.message }, 400);
	}
	return json({ success: true });
}
