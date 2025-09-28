# 🚀 Deployment Guide - Mystic Forest Adventure

This guide will help you deploy your Forest Adventure Game to GitHub and Vercel.

## 📋 Prerequisites

- GitHub account
- Vercel account (free)
- Git installed locally
- Python 3.7+ installed

## 🔧 Step 1: Prepare Your Repository

### 1.1 Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: Forest Adventure Game with Flow integration"
```

### 1.2 Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New repository"
3. Name it: `mystic-forest-adventure`
4. Make it public
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### 1.3 Push to GitHub
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/mystic-forest-adventure.git

# Push your code
git branch -M main
git push -u origin main
```

## 🌐 Step 2: Deploy to Vercel

### 2.1 Connect to Vercel
1. Go to [Vercel.com](https://vercel.com)
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your `mystic-forest-adventure` repository
5. Click "Import"

### 2.2 Configure Vercel
Vercel should auto-detect your configuration from `vercel.json`:

- **Framework Preset**: Other
- **Root Directory**: `./` (default)
- **Build Command**: (leave empty)
- **Output Directory**: (leave empty)

### 2.3 Deploy
1. Click "Deploy"
2. Wait for deployment to complete (2-3 minutes)
3. You'll get a URL like: `https://mystic-forest-adventure-xxx.vercel.app`

## ✅ Step 3: Verify Deployment

### 3.1 Test Your Live Site
1. Open your Vercel URL
2. Play through the game
3. Test blockchain features (if MetaMask is connected)

### 3.2 Check Vercel Dashboard
- Go to your Vercel dashboard
- Check deployment logs for any errors
- Monitor function invocations

## 🔄 Step 4: Continuous Deployment

### 4.1 Automatic Deployments
- Every push to `main` branch triggers automatic deployment
- Vercel will build and deploy your changes automatically

### 4.2 Manual Deployments
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from your project directory
vercel

# Deploy to production
vercel --prod
```

## 🐛 Troubleshooting

### Common Issues:

#### 1. **Build Failures**
- Check Vercel logs in dashboard
- Ensure `requirements.txt` has all dependencies
- Verify Python version compatibility

#### 2. **Static Files Not Loading**
- Check `vercel.json` routes configuration
- Ensure files are in `public/` directory
- Verify file paths in HTML

#### 3. **API Endpoints Not Working**
- Check Flask app configuration
- Verify CORS settings
- Test endpoints individually

#### 4. **Blockchain Features Not Working**
- Ensure MetaMask is installed
- Check browser console for errors
- Verify contract address is correct

## 📊 Monitoring

### Vercel Analytics
- View deployment metrics
- Monitor function performance
- Check error rates

### GitHub Actions (Optional)
You can add GitHub Actions for automated testing:

```yaml
# .github/workflows/test.yml
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Test
        run: python test-server.py
```

## 🎯 Production Checklist

- [ ] Repository is public on GitHub
- [ ] Vercel deployment is successful
- [ ] All game features work on live site
- [ ] Blockchain integration works
- [ ] Images load correctly
- [ ] Mobile responsive design works
- [ ] README is updated with live URL
- [ ] Smart contract is deployed and verified

## 🔗 Useful Links

- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Pages](https://pages.github.com)
- [Flow Testnet Explorer](https://evm-testnet.flowscan.io)
- [MetaMask Documentation](https://docs.metamask.io)

## 🎉 Success!

Once deployed, your Forest Adventure Game will be live and accessible to anyone with the URL. Players can:

1. Play the interactive story
2. Generate AI images
3. Save their adventures to Flow blockchain
4. Share their results

Your project is now ready for the ETHGlobal submission! 🏆
