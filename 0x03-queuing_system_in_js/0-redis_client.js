import redis from 'redis';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));
