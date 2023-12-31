import kue from 'kue';

const queue = kue.createQueue();
blackList = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (phoneNumber in blackList)
    job.failed()
  console.log('Sending notification to', phoneNumber, 'with message:', message);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
