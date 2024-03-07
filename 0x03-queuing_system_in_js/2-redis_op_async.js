#!/usr/bin/node
import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();

client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, print);
}
async function displaySchoolValue(schoolName) {
    const GET = promisify(client.GET).bind(client);
    try {
      const value = await GET(schoolName);
      console.log(value);
    } catch (error) {
      console.log(error.toString());
    }
  }

async function runOperations() {
    try {
        await displaySchoolValue('Holberton');
        await setNewSchool('HolbertonSanFrancisco', '100');
        await displaySchoolValue('HolbertonSanFrancisco');
    } catch (error) {
        console.error(error);
    }
}

runOperations();

