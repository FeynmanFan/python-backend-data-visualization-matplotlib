const express = require('express');
const diskusage = require('diskusage');
const os = require('os');
const fs = require('fs').promises; 
const path = require('path');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/getdrivespace', async (req, res) => {
    const drive = req.query.drive;

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

app.get('/getresponsetimes', async (req, res) => {
    try {
        const filePath = path.join(__dirname, 'responsetimes.json');
        const data = await fs.readFile(filePath, 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.status(500).send(`Error reading file: ${error.message}`);
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});