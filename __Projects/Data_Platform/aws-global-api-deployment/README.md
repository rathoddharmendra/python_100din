# AWS Global API Deployment

This repo deploys two Flask APIs to AWS (Frankfurt and Mumbai), sets up ALBs, and configures Route 53 latency-based DNS.


--- commands

Shers-MacBook-Air:aws-global-api-deployment mac_dee$ history | tail -n 20
  505  lsof -i 9000
  507  kill -9 28866
  514  ps -p 594 -o comm,cmd
  515  ps -e | wc -l