#!/usr/bin/node
/**
 * Writing the test for job creation
 */
import { createQueue } from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;

const queue = createQueue();


it('checking if not an array input', function () {
    expect(function () { createPushNotificationsJobs(1, queue) }).to.throw(/Jobs is not an array/);
});