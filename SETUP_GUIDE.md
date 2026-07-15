# PhoneHub Complete Setup Guide
## From Zero to Production in 35 Minutes

---

## 📋 Prerequisites

- Python 3.8+ installed
- GitHub account (for hosting)
- 15 minutes to sign up for free APIs

---

## 🚀 Quick Start (Free Tier Only)

### Step 1: Clone and Setup (2 minutes)

```bash
cd _deploy_staging/phonehub/tools
```

### Step 2: Get Free API Keys (15 minutes total)

#### A. Rainforest API (Amazon prices) - **5 minutes**
1. Go to https://www.rainforestapi.com
2. Click "Get Started Free"
3. Sign up with email
4. Verify email
5. Copy API key from dashboard
6. **Free tier: 1,000 requests/month** (enough for 200+ products)

#### B. ScraperAPI (GSMArena specs) - **3 minutes**
1. Go to https://www.scraperapi.com
2. Click "Start Free Trial"
3. Sign up (no credit card required)
4. Copy API key from dashboard
5. **Free tier: 5,000 requests/month**

#### C. Bing Image Search API - **5 minutes**
1. Go to https://portal.azure.com
2. Create free account (no credit card for free tier)
3. Search "Bing Search v7"
4. Create resource → Select "Free F1" tier
5. Go to "Keys and Endpoint" → Copy Key 1
6. **Free tier: 1,000 searches/month**

#### D. Pexels API (Backup images) - **2 minutes**
1. Go to https://www.pexels.com/api/
2. Click "Get Started"
3. Sign up and verify email
4. Create new API key
5. **Free tier: Unlimited**

---

### Step 3: Configure API Keys (3 minutes)

Create `config.json` from template:

```bash
cd _deploy_staging/phonehub/tools
cp config.enhanced.json config.json
```

Edit `config.json` and add your keys:

```json
{
  "site_url": "https://jahid124421.github.io/phonehub",
  
  "scraperapi_key": "YOUR_SCRAPERAPI_KEY_HERE",
  "rainforest_api_key": "YOUR_RAINFOREST_KEY_HERE",
  "bing_image_api_key": "YOUR_BING_KEY_HERE",
  "pexels_api_key": "YOUR_PEXELS_KEY_HERE",
  
  "newsapi_key": "ea5d3f63e0f74c2cb89755f3e1505326",
  
  "llm": {
    "provider": "openrouter",
    "model": "meta-llama/llama-3.3-70b-instruct",
    "keys_env_path": "../../ai-bots-package/my-keys.env"
  },
  
  "affiliate": {
    "amazon_partner_tag": "",
    "amazon_marketplace": "www.amazon.com"
  }
}
```

**Or use environment variables:**

```bash
# Windows
set SCRAPERAPI_KEY=your_key_here
set RAINFOREST_API_KEY=your_key_here
set BING_IMAGE_API_KEY=your_key_here
set PEXELS_API_KEY=your_key_here

# Linux/Mac
export SCRAPERAPI_KEY=your_key_here
export RAINFOREST_API_KEY=your_key_here
export BING_IMAGE_API_KEY=your_key_here
export PEXELS_API_KEY=your_key_here
```

---

### Step 4: Run Initial Build (10 minutes)

```bash
# First run: Seed catalog with Wikidata (fast, free)
python wikidata_seed.py --all

# Enhance specs with GSMArena details (uses ScraperAPI)
python import_specs_enhanced.py --limit 50

# Fetch real prices (uses Rainforest API)
python price_job_enhanced.py --limit 50

# Fetch high-quality images (uses Bing + Pexels)
python image_fetcher.py --limit 50

# Generate AI reviews
python content_agent.py --limit 50

# Build final data files
python build.py
```

**Result:** 50+ products with specs, prices, images, and reviews!

---

### Step 5: Deploy to GitHub Pages (5 minutes)

```bash
cd ../../..  # back to repo root

# Commit and push
git add .
git commit -m "Initial catalog with real data"
git push origin main
```

GitHub Actions will automatically:
- Build the site
- Deploy to GitHub Pages
- Submit to IndexNow (Bing/Yandex)

**Your site is now live!** 🎉

---

## 🔄 Automated Daily Updates

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs daily and:

1. Seeds new products from Wikidata
2. Enhances specs for new items
3. Updates prices
4. Fetches images for new products
5. Generates reviews
6. Rebuilds site
7. Deploys
8. Pings search engines

**You don't need to do anything!**

---

## 📊 Monitor Your Free Tier Usage

### Rainforest API
- Dashboard: https://dashboard.rainforestapi.com
- 1,000 requests/month = ~33/day
- **Recommendation:** Run price updates every 3 days

### ScraperAPI
- Dashboard: https://dashboard.scraperapi.com
- 5,000 requests/month = ~166/day
- **Recommendation:** Import 20 new phones/day

### Bing Images
- Azure Portal: https://portal.azure.com
- 1,000 requests/month = ~33/day
- **Recommendation:** Fetch images for new products only

### Pexels
- No limits!
- Use as primary fallback for missing images

---

## 🎯 SEO Setup (10 minutes)

### Google Search Console
1. Go to https://search.google.com/search-console
2. Add property: `https://jahid124421.github.io/phonehub/`
3. Verify via HTML file upload (download from console)
4. Submit sitemap: `https://jahid124421.github.io/phonehub/sitemap.xml`
5. Request indexing for top 10 pages

### Bing Webmaster Tools
1. Go to https://www.bing.com/webmasters
2. Add site (already indexed via IndexNow!)
3. Submit sitemap: `https://jahid124421.github.io/phonehub/sitemap.xml`

### Result
- Google: Indexed in 3-7 days
- Bing: Indexed in 24-48 hours (via IndexNow)

---

## 💰 Monetization Setup

### Amazon Associates (After Domain)
1. Buy custom domain (see Domain Setup below)
2. Go to https://affiliate-program.amazon.com
3. Apply with your domain
4. Add "About", "Privacy Policy", "Terms" pages (already done!)
5. Wait 24-48 hours for approval
6. Add your tag to `config.json`:
   ```json
   "affiliate": {
     "amazon_partner_tag": "yoursite-20"
   }
   ```

### Flipkart Affiliate (India)
1. Go to https://affiliate.flipkart.com
2. Sign up
3. Get tracking ID
4. Add to config:
   ```json
   "affiliate": {
     "flipkart_affiliate_id": "your_id"
   }
   ```

---

## 🌐 Domain Setup (Recommended)

### Why?
- **10x better SEO** than github.io subdomain
- Required for Amazon Associates approval
- Professional appearance
- Custom email (with some registrars)

### Where to Buy ($10-15/year)
1. **Namecheap** (recommended): https://www.namecheap.com
   - $8.98/year for .com
   - Free WhoisGuard (privacy)
2. **Cloudflare**: https://www.cloudflare.com/products/registrar/
   - $9.77/year (at-cost pricing)
   - Built-in DDoS protection
3. **Google Domains** (now Squarespace): https://domains.squarespace.com
   - $12/year

### Suggested Domains
- `phonehub.tech` (available, $12/yr)
- `gadgethub.tech` (available, $12/yr)
- `techspecs.store` (available, $10/yr)
- `pricecompare.tech` (available, $12/yr)

### GitHub Pages Setup
1. Buy domain
2. Add DNS records at registrar:
   ```
   Type: A
   Name: @
   Value: 185.199.108.153
   
   Type: A
   Name: @
   Value: 185.199.109.153
   
   Type: A
   Name: @
   Value: 185.199.110.153
   
   Type: A
   Name: @
   Value: 185.199.111.153
   
   Type: CNAME
   Name: www
   Value: jahid124421.github.io
   ```
3. In GitHub repo: Settings → Pages → Custom domain → Enter your domain
4. Enable "Enforce HTTPS" (wait 24h for certificate)
5. Update `config.json`:
   ```json
   "site_url": "https://yourdomain.com"
   ```
6. Rebuild and deploy

**Done!** Your site is now at your custom domain.

---

## 🔧 Advanced Options (Optional)

### Keepa API (Reliable Prices)
- **Cost:** €19/month
- **Value:** Best Amazon price tracking
- **When:** After revenue > €30/month
- **Setup:** https://keepa.com/#!api

### PriceAPI (Multi-Retailer)
- **Cost:** $29/month (or free 100/day)
- **Value:** Walmart, Best Buy, etc.
- **When:** Expanding beyond Amazon
- **Setup:** https://www.priceapi.com

### Unsplash API (Premium Images)
- **Cost:** Free 50/hour
- **Value:** High-quality stock photos
- **Note:** Pexels is unlimited, use that first
- **Setup:** https://unsplash.com/developers

---

## 📈 Scaling Strategy

### Month 1 (Free Tier)
- **Traffic:** 0-100 visitors/day
- **Products:** 200-300 (via Wikidata + GSMArena)
- **Cost:** $0 (maybe $2 for OpenRouter)
- **Focus:** SEO, content quality

### Month 2-3 (Custom Domain)
- **Traffic:** 100-500 visitors/day
- **Products:** 500-800
- **Cost:** $10/year domain
- **Focus:** Amazon Associates approval, social sharing

### Month 4-6 (First Revenue)
- **Traffic:** 500-2,000 visitors/day
- **Revenue:** $10-50/month (affiliate commissions)
- **Products:** 1,000-1,500
- **Cost:** Still free tier APIs
- **Focus:** Content expansion (comparisons, guides)

### Month 7+ (Growth Phase)
- **Traffic:** 2,000-10,000+ visitors/day
- **Revenue:** $100-500+/month
- **Products:** 2,000+
- **Cost:** Upgrade to Keepa API (€19/mo)
- **Focus:** Scale content, add more categories

---

## 🆘 Troubleshooting

### API Key Not Working
- Check spelling and spaces
- Verify key is active in provider dashboard
- Try environment variable instead of config file
- Check API usage quota

### No Prices Showing
- Verify Rainforest API key is valid
- Check product name format (try shorter query)
- Fallback: Affiliate links still work (no price, but earn commission)

### Images Not Loading
- Verify Bing API key subscription is active
- Check Pexels API key
- Wikidata images should still work (fallback)

### Build Fails
- Check Python version: `python --version` (need 3.8+)
- Verify all tools/*.py files are present
- Check config.json syntax (use JSON validator)

### GitHub Actions Failing
- Check Actions tab for error logs
- Verify API keys are in repo secrets (not config.json in GitHub)
- Check quota limits

---

## 📞 Support Resources

- **PhoneHub Issues:** https://github.com/jahid124421/phonehub/issues
- **Rainforest API Docs:** https://www.rainforestapi.com/docs
- **ScraperAPI Docs:** https://docs.scraperapi.com
- **Bing Search Docs:** https://docs.microsoft.com/en-us/bing/search-apis/
- **GitHub Pages Docs:** https://docs.github.com/en/pages

---

## ✅ Success Checklist

- [ ] All API keys obtained (Rainforest, ScraperAPI, Bing, Pexels)
- [ ] config.json configured with keys
- [ ] Initial build completed (50+ products)
- [ ] Site deployed to GitHub Pages
- [ ] Google Search Console verified
- [ ] Bing Webmaster Tools setup
- [ ] Sitemap submitted to both
- [ ] Custom domain purchased (recommended)
- [ ] Domain DNS configured
- [ ] Amazon Associates applied (after domain)
- [ ] Automated daily updates working

**Congratulations!** 🎉 Your site is production-ready!

---

## 🎯 Next Steps

1. Create comparison pages ("iPhone 15 vs Samsung S24")
2. Write buying guides ("Best phones under $500")
3. Share on social media (Reddit, Twitter, FB groups)
4. Monitor Search Console for keyword opportunities
5. Add more categories (tablets, laptops, watches)
6. Consider AdSense when traffic > 1,000/day

**You're now ready to launch!** 🚀
