import kue from 'kue';

const queue = kue.createQueue();
const data = {phoneNumber: '001', message: 'msg goes here'};
const job = queue.create('push_notification_code', data).save((err) => {
  if( !err ) console.log('Notification job created:', job.id);
});

job.on('complete', (res) => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed');
});
