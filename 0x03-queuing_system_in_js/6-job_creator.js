#!/usr/bin/node

import { createQueue } from "kue";

const queue = createQueue();
const data = { phoneNumber: '123456789', message: 'A test message' }

const job = queue.create('push_notification_code', data)
    .save(function (error) {
        if (!error) {
            console.log(`Notification job created: ${job.id}`);
        }
    });

job.on('complete', function () {
    console.log('Notification job completed')
});
job.on('failed', function () {
    console.log('Notification job failed');
});
