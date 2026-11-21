# SelfHostLab

Self-hosted apps measured on a real VPS (RAM, CPU, disk), with the commands to reproduce each number.

- n8n 2.35.7 measurements: [data/n8n-2.35.7-measurements.csv](data/n8n-2.35.7-measurements.csv), load script [data/load.py](data/load.py), workflow [wf.json](n8n-self-hosted-requirements/wf.json)
- Write-up: https://selfhostlab.org/n8n-self-hosted-requirements/

Test host: 8 AMD EPYC vCPU, 23 GB RAM, Node.js 22.22.2, n8n installed with npm, SQLite, default task runner. RSS of main process + task runner sampled every 0.3 s with `ps`.
