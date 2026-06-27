# helloworld

Built with python on 2026-06-27

## Local Development

```bash
# Run locally
docker compose up --build

# Or natively (language-specific)
# python: see project docs for local run instructions
```

## Deployment

Deployed to Portainer via Ansible:

```bash
# From HackFortress root:
ansible-playbook playbooks/deploy_helloworld.yml -i inventories/prod.yaml
```

## Health Check

```bash
curl http://<host>:8080/health
```
