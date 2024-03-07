#!/usr/bin/node
function createPushNotificationsJobs(jobs, queue) {
    if (!(jobs instanceof Array)) {
        throw new Error('Jobs is not an array');
    }
    for (let job of jobs) {
        job = queue.create('push_notification_code_3', job);
        job
            .on('complete', function (res) {
                console.log(`Notification job ${job.id} completed`);
            })
            .on('failed', function (err) {
                console.log(`Notification job ${job.id} failed: ${err.message || err.toString()}`);
            })
            .on('progress', function (progress, data) {
                console.log(`Notification job ${job.id} ${progress}% complete`);
            })
            .save(function (err) {
                console.log(`Notification job created: ${job.id}`);
            });
    }
}

module.exports = createPushNotificationsJobs;