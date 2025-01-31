const express = require('express');
const diskusage = require('diskusage');
const os = require('os');
const fs = require('fs').promises; // Using Promises for file operations
const path = require('path');
const app = express();
const port = 3000;

// Middleware for parsing JSON bodies
app.use(express.json());

// Route for getting drive space
app.get('/getdrivespace', async (req, res) => {
    const drive = req.query.drive; // Assuming drive name is passed as a query parameter

    if (!drive) {
        return res.status(400).send('Drive parameter is required');
    }

    try {
        const info = await diskusage.check(drive);
        res.json({
            total: info.total,
            available: info.available
        });
    } catch (error) {
        res.status(500).send(`Error checking drive: ${error.message}`);
    }
});

// Route for getting CPU usage
app.get('/getCPUUsage', (req, res) => {
    const cpus = os.cpus();
    let totalIdle = 0, totalTick = 0;
    
    for (let i = 0, len = cpus.length; i < len; i++) {
        const cpu = cpus[i];
        for (let type in cpu.times) {
            totalTick += cpu.times[type];
        }
        totalIdle += cpu.times.idle;
    }

    const totalUsage = (100 - (100 * totalIdle) / totalTick).toFixed(2);

    res.json({
        cpuUsage: totalUsage + '%'
    });
});

// New Route for getting response times from JSON file
app.get('/getresponsetimes', async (req, res) => {
    try {
        // Assuming the JSON file is named 'data.json' and is in the same directory as your server script
        const filePath = path.join(__dirname, 'data.json');
        const data = await fs.readFile(filePath, 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.status(500).send(`Error reading file: ${error.message}`);
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});