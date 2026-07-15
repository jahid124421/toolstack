# GitHub Actions Setup for PhoneHub

## Overview
GitHub Actions will automatically run your pipeline daily and deploy to GitHub Pages.

---

## 🔐 Add API Keys as Secrets

### Step 1: Go to Repository Settings
1. Open your GitHub repository
2. Click **Settings** (top right)
3. In left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**

### Step 2: Add Each API Key

Add the following secrets (one at a time):

#### Required Secrets (Minimum Setup)

| Secret Name | Value | Where to Get |
|-------------|-------|--------------|
| `RAINFOREST_API_KEY` | Your API key | https://www.rainforestapi.com |
| `BING_IMAGE_API_KEY` | Your API key | https://portal.azure.com |
| `OPENROUTER_API_KEY` | Your API key | https://openrouter.ai |

#### Optional Secrets (Enhanced Features)

| Secret Name | Value | Where to Get |
|-------------|-------|--------------|
| `SCRAPERAPI_KEY` | Your API key | https://www.scraperapi.com |
| `RAPIDAPI_KEY` | Your API key | https://rapidapi.com |
| `KEEPA_API_KEY` | Your API key | https://keepa.com/#!api |
| `PRICEAPI_KEY` | Your API key | https://www.priceapi.com |
| `PEXELS_API_KEY` | Your API key | https://www.pexels.com/api/ |
| `UNSPLASH_API_KEY` | Your API key | https://unsplash.com/developers |
| `NEWSAPI_KEY` | Your API key | https://newsapi.org |

For each secret:
1. Click **New repository secret**
2. Name: Enter the secret name exactly as shown above
3. Value: Paste your API key
4. Click **Add secret**

---

## 📝 Update GitHub Actions Workflow

Edit `.github/workflows/deploy.yml` to use the secrets:

```yaml
name: Deploy PhoneHub

on:
  push:
    branches: [ main ]
  schedule:
    # Run daily at 2 AM UTC
    - cron: '0 2 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Run Enhanced Pipeline
      env:
        # Required
        RAINFOREST_API_KEY: ${{ secrets.RAINFOREST_API_KEY }}
        BING_IMAGE_API_KEY: ${{ secrets.BING_IMAGE_API_KEY }}
        OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        
        # Optional
        SCRAPERAPI_KEY: ${{ secrets.SCRAPERAPI_KEY }}
        RAPIDAPI_KEY: ${{ secrets.RAPIDAPI_KEY }}
        KEEPA_API_KEY: ${{ secrets.KEEPA_API_KEY }}
        PRICEAPI_KEY: ${{ secrets.PRICEAPI_KEY }}
        PEXELS_API_KEY: ${{ secrets.PEXELS_API_KEY }}
        UNSPLASH_API_KEY: ${{ secrets.UNSPLASH_API_KEY }}
        NEWSAPI_KEY: ${{ secrets.NEWSAPI_KEY }}
      run: |
        cd _deploy_staging/phonehub/tools
        python run_all_enhanced.py --limit 100
    
    - name: Copy Built Files
      run: |
        python copy_for_deploy.py
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./deploy_output
        cname: yourdomain.com  # Optional: add your custom domain here
```

---

## ⚙️ Workflow Triggers

The workflow runs:
1. **On every push** to `main` branch
2. **Daily at 2 AM UTC** (auto-updates catalog)
3. **Manually** via "Actions" tab → "Run workflow"

---

## 🧪 Test the Workflow

### Option 1: Manual Trigger
1. Go to **Actions** tab in GitHub
2. Click on "Deploy PhoneHub" workflow
3. Click **Run workflow** button
4. Select branch: `main`
5. Click **Run workflow**

### Option 2: Push a Commit
```bash
git add .
git commit -m "Test GitHub Actions"
git push origin main
```

### Check Progress
1. Go to **Actions** tab
2. Click on the running workflow
3. Watch real-time logs

---

## 📊 Monitor Usage

### API Usage Dashboard Links

After setup, monitor your usage:

| Service | Dashboard |
|---------|-----------|
| Rainforest API | https://dashboard.rainforestapi.com |
| ScraperAPI | https://dashboard.scraperapi.com |
| Bing API | https://portal.azure.com |
| Keepa | https://keepa.com/#!api |
| PriceAPI | https://www.priceapi.com/dashboard |
| Pexels | No usage limits |
| Unsplash | https://unsplash.com/oauth/applications |
| NewsAPI | https://newsapi.org/account |

---

## 🚨 Troubleshooting

### Workflow Fails with "Secret not found"
- Check secret names match exactly (case-sensitive)
- Verify secrets are added in **Actions** section, not **Environments**

### Workflow Fails with "API Key Invalid"
- Test key locally first: `python run_all_enhanced.py --quick`
- Check key hasn't expired
- Verify key has correct permissions

### Workflow Runs but No Changes
- Check if `--limit` in workflow is too low
- Verify `copy_for_deploy.py` is working
- Check deploy step logs for errors

### Rate Limit Exceeded
- Reduce `--limit` in workflow (e.g., `--limit 50`)
- Change schedule to run less frequently:
  ```yaml
  schedule:
    - cron: '0 2 */3 * *'  # Every 3 days
  ```

---

## 💡 Best Practices

### 1. Gradual Rollout
Start with small limits and increase:
```yaml
# Week 1
run: python run_all_enhanced.py --limit 20

# Week 2
run: python run_all_enhanced.py --limit 50

# Week 3+
run: python run_all_enhanced.py --limit 100
```

### 2. Monitor Costs
Set up alerts in provider dashboards:
- Rainforest: Alert at 800/1000 requests
- ScraperAPI: Alert at 4000/5000 requests

### 3. Backup Data
Add a backup step to workflow:
```yaml
- name: Backup Data
  run: |
    mkdir -p backups
    cp _deploy_staging/phonehub/data/*.json backups/
    
- name: Upload Backup
  uses: actions/upload-artifact@v3
  with:
    name: data-backup
    path: backups/
    retention-days: 30
```

### 4. Separate Staging and Production
Create two workflows:
- `staging.yml` - Runs on `develop` branch, uses test keys
- `deploy.yml` - Runs on `main` branch, uses production keys

---

## 🎯 Complete Example Workflow

```yaml
name: PhoneHub Enhanced Pipeline

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        cache: 'pip'
    
    - name: Run Enhanced Pipeline
      env:
        RAINFOREST_API_KEY: ${{ secrets.RAINFOREST_API_KEY }}
        SCRAPERAPI_KEY: ${{ secrets.SCRAPERAPI_KEY }}
        BING_IMAGE_API_KEY: ${{ secrets.BING_IMAGE_API_KEY }}
        PEXELS_API_KEY: ${{ secrets.PEXELS_API_KEY }}
        OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        NEWSAPI_KEY: ${{ secrets.NEWSAPI_KEY }}
      run: |
        cd _deploy_staging/phonehub/tools
        python run_all_enhanced.py --limit 100
    
    - name: Prepare Deployment
      run: python copy_for_deploy.py
    
    - name: Deploy to Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./deploy_output
        force_orphan: true
    
    - name: Notify Success
      if: success()
      run: echo "✓ Deployment successful! Site updated."
    
    - name: Notify Failure
      if: failure()
      run: echo "✗ Deployment failed. Check logs above."
```

---

## ✅ Setup Checklist

- [ ] API keys obtained from providers
- [ ] Secrets added to GitHub (Settings → Secrets → Actions)
- [ ] Workflow file created/updated (`.github/workflows/deploy.yml`)
- [ ] Test run successful (Actions tab → Run workflow)
- [ ] Daily schedule verified (check next scheduled run)
- [ ] Usage monitoring dashboards bookmarked
- [ ] Backup strategy in place

**You're all set!** 🎉

Your site will now:
- Update automatically every day
- Fetch new products from Wikidata
- Get real prices from Amazon
- Download high-quality images
- Generate AI reviews
- Deploy to GitHub Pages
- All without manual intervention!
