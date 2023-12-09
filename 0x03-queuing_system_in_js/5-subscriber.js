import redis from 'redis';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

const listener = (channel, message) => {
  console.log(message);
  if (message == 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
}
client.subscribe('holberton school channel');
client.on('message', listener);
