/* config MongoDB */

const database = 'Web-Scraping';
const collections = ['User', 'Product'];

// Create a new database.
use(database);

// Create a user collection.
db.createCollection(collections[0]);

// Create a product collection.
db.createCollection(collections[1]);

