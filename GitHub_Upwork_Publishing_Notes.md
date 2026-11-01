# Publishing and portfolio notes (separate from technical PDFs)

## Repository

Public repository: https://github.com/riaxkhan007/docker-compose-nginx-ubuntu

The repository already exists. Your local Ubuntu project directory is `~/projects/docker-compose-nginx-ubuntu` and your SSH remote is already configured. First transfer the downloaded ZIP from Windows PowerShell to Ubuntu. Replace the example IP with the current result of `hostname -I`:

```powershell
scp "$env:USERPROFILE\Downloads\docker-compose-nginx-ubuntu-complete-package.zip" riaxkhan@192.168.109.129:/home/riaxkhan/
```

On Ubuntu, inspect and extract the archive outside the existing Git repository:

```bash
mkdir -p ~/package-review
unzip ~/docker-compose-nginx-ubuntu-complete-package.zip -d ~/package-review
find ~/package-review/docker-compose-nginx-ubuntu -maxdepth 3 -type f | sort
```

Back up the existing project, then copy the reviewed package files into it. The archive does not contain your `.git` directory, so your existing Git history and `origin` remote remain in place:

```bash
cp -a ~/projects/docker-compose-nginx-ubuntu ~/projects/docker-compose-nginx-ubuntu-backup-$(date +%F-%H%M)
cp -a ~/package-review/docker-compose-nginx-ubuntu/. ~/projects/docker-compose-nginx-ubuntu/
```

Now validate the project and inspect the changed files:

```bash
cd ~/projects/docker-compose-nginx-ubuntu
sudo docker compose config
sudo docker compose up -d --build
sudo docker compose ps
curl -i http://localhost/
curl -i http://localhost/health
curl -i http://localhost/nginx-health
git status --short
git remote -v
```

Only after reviewing `git status`, stage, commit, and push:

```bash
git add .
git status
git commit -m "Document Docker Compose Flask deployment with Nginx"
git push origin main
```

Do not commit secrets, SSH private keys, `.env` files, or personal data. If Git reports there is nothing to commit, inspect the repository on GitHub to confirm the files are already present.

If the branch has diverged, stop and inspect before using pull/rebase or force-push. Never force-push just to clear an error.

## Final GitHub check

Open the repository URL and verify that the README renders, the architecture image loads, source/config files are visible, and the latest commit appears. Confirm the repository is public only if you intend the code to be publicly viewable. Keep credentials and private infrastructure details out of the repo.

## Suggested portfolio project information

**Title:** Docker Compose Flask Deployment with Nginx Reverse Proxy

**Role:** Linux / Docker Deployment Engineer

Upwork's current profile guidance lists limits of 70 characters for the title, 100 for the role, and 600 for the project description. The suggested fields below fit those limits.

**Description:** Deployed a containerized Python Flask application on Ubuntu using Docker Compose and Nginx as a reverse proxy. Built a custom Python image, ran the application with Gunicorn under a non-root user, and connected services through a dedicated Docker bridge network. Configured HTTP routing, forwarded client headers, and health endpoints. Documented deployment, validation, and troubleshooting procedures.

**Skills to select:** Linux Administration, Ubuntu, Docker, Docker Compose, Nginx, Python, Flask, Gunicorn, Reverse Proxy, Networking, TCP/IP.

Only select skills that accurately reflect what is implemented and demonstrated.

## Upwork portfolio upload notes

1. Open your freelancer profile and find the **Portfolio** section. Select its add/plus control and create a portfolio item.
2. Enter the title, role, description, and relevant skills. The current Upwork help page lists maximums of 70, 100, and 600 characters for title, role, and description respectively.
3. Upload `assets/project-cover.png` as the cover image. It is 1000 x 750 pixels, matching Upwork's recommended image dimensions. Add genuine screenshots from `screenshots/` after capturing them from the working environment. A PDF is not a substitute for the image/video cover.
4. Add the GitHub repository URL in the project URL/link field if the current form offers one.
5. Attach the Technical Guide PDF as supporting documentation where the form permits it. The separate Configuration Reference PDF can be a second attachment if the upload area supports it. Both supplied PDFs are below 2 MB and contain neutral technical documentation without marketplace labels or contact information.
6. Review the preview and publish the portfolio item. Use the project's **Share** link to copy a public link after it is published.
- Use a short, accurate description. Do not claim HTTPS, a public production deployment, Kubernetes, CI/CD, monitoring, or high availability; these are not part of this implementation.
- When submitting a proposal, use Profile highlights to attach the published portfolio item when that option is available. A repository link can also be included where the job form permits it.
- For messages to an existing client, Upwork Messages supports file attachments. Prefer the portfolio link for reusable work samples and attach the PDF only when it helps the conversation.

Upwork's help pages distinguish upload areas: one portfolio-item article lists PDF documents up to 25 MB, while its PDF work-sample guidance says up to two PDFs under 2 MB each. To avoid friction, these supplied PDFs are each under 2 MB. Check the exact limit shown by the upload screen because Upwork's limits and interface can change.

For a proposal, select **Apply now**, complete the proposal details, then use **Profile highlights** to attach the published portfolio item when that option is available. Upwork Messages can also send a PDF with the paperclip attachment control. Use the published portfolio link for a reusable sample; send an attached PDF in a message only when it is useful in that specific conversation.

Official help pages: [Enhance your freelancer profile](https://support.upwork.com/hc/en-us/articles/360016144974-How-to-enhance-your-freelancer-profile), [Portfolio publishing requirements](https://support.upwork.com/hc/en-us/articles/39295662788115-Why-won-t-my-portfolio-item-publish), [PDF work samples](https://support.upwork.com/hc/en-us/articles/4406143264531-How-to-choose-PDF-work-samples-for-your-project), [Share a portfolio project](https://support.upwork.com/hc/en-us/articles/39295510081811-How-can-I-share-my-portfolio-project), and [Share documents in Upwork Messages](https://support.upwork.com/hc/en-us/articles/360049608113-How-to-share-documents-files-and-more-on-Upwork).

## Evidence to capture before publishing

1. Browser homepage through Nginx.
2. `/health` JSON response.
3. `/nginx-health` response.
4. `sudo docker compose ps` showing both services Up.
5. `sudo docker compose run --rm nginx nginx -t` showing syntax/test successful.

Capture real output only. Redact any credentials and avoid showing irrelevant personal or internal information.
