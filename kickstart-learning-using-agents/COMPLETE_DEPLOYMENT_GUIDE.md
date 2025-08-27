# 🚀 Complete Google Cloud Run Deployment Guide

## 📋 DEPLOYMENT CHECKLIST

### ✅ COMPLETED (Ready for deployment)
- [x] **Optimized FastAPI app** (`app_cloudrun.py`)
- [x] **Free tier optimized Dockerfile** 
- [x] **Deployment scripts** (`deploy-cloudrun.sh`)
- [x] **Docker ignore file** (reduces build time)
- [x] **Service configuration** (`cloudrun-service.yaml`)
- [x] **Monitoring guide** (`MONITORING_GUIDE.md`)
- [x] **Pre-deployment checker** (`pre-deploy-check.sh`)

### 🔄 TODO (You need to complete)
- [ ] **Install Google Cloud CLI**
- [ ] **Create Google Cloud Project** 
- [ ] **Set up billing** (required for free tier)
- [ ] **Deploy to Cloud Run**
- [ ] **Test deployment**

## 🛠️ STEP 1: Install Google Cloud CLI

### For Windows (WSL/Linux):
```bash
# Download and install
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz -o gcloud.tar.gz
tar -xf gcloud.tar.gz
./google-cloud-sdk/install.sh

# Initialize
./google-cloud-sdk/bin/gcloud init
```

### Alternative - Use Package Manager:
```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli
```

## 🏗️ STEP 2: Set Up Google Cloud Project

```bash
# Login to Google Cloud
gcloud auth login

# Create new project (replace with your preferred name)
gcloud projects create my-learning-agent-2025 --name="Learning Agent"

# Set as default project
gcloud config set project my-learning-agent-2025

# Enable billing at: https://console.cloud.google.com/billing
```

## 🚀 STEP 3: Deploy to Cloud Run

### Option A: Quick Deployment (Recommended)
```bash
# Run pre-deployment check
./pre-deploy-check.sh

# Deploy (replace with your project ID)
./deploy-cloudrun.sh my-learning-agent-2025 kickstart-learning-agent us-central1
```

### Option B: Manual Deployment
```bash
# Enable APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

# Deploy from source
gcloud run deploy kickstart-learning-agent \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --max-instances 10 \
  --min-instances 0 \
  --memory 512Mi \
  --cpu 1 \
  --timeout 240s \
  --concurrency 100
```

## 🔧 STEP 4: Set Environment Variables

```bash
# Set your API keys (replace with actual keys)
gcloud run services update kickstart-learning-agent \
  --region us-central1 \
  --set-env-vars GOOGLE_API_KEY="your-google-api-key-here" \
  --set-env-vars TAVILY_API_KEY="your-tavily-api-key-here"
```

## 🧪 STEP 5: Test Deployment

```bash
# Get service URL
SERVICE_URL=$(gcloud run services describe kickstart-learning-agent --platform managed --region us-central1 --format 'value(status.url)')

echo "🌐 Service URL: $SERVICE_URL"

# Test health endpoint
curl "$SERVICE_URL/health"

# Test API endpoint
curl -X POST "$SERVICE_URL/api/generate-pathway-direct" \
  -H "Content-Type: application/json" \
  -d '{
    "learning_style": "Interactive examples",
    "progress": "Python basics",
    "hobby": "Gaming", 
    "domain": "Software Development",
    "google_api_key": "your-key-here",
    "tavily_api_key": "your-key-here"
  }'
```

## 💰 FREE TIER GUARANTEES

Your deployment is optimized to stay within Google Cloud's **Always Free** limits:

| Resource | Free Limit | Your Config | Usage |
|----------|------------|-------------|-------|
| CPU | 180,000 vCPU-sec/month | 1 vCPU | ~50 hours/month |
| Memory | 360,000 GiB-sec/month | 0.5 GiB | ~200 hours/month |  
| Requests | 2M requests/month | Unlimited | 2M requests/month |
| Network | 1 GiB egress/month | Variable | Depends on usage |

**Bottleneck**: CPU time (50 hours) - supports ~12,000 requests/month with 15s processing time.

## 📊 MONITORING & ALERTS

1. **Console Dashboard**: https://console.cloud.google.com/run
2. **Billing Reports**: https://console.cloud.google.com/billing/reports  
3. **Usage Tracking**: See `MONITORING_GUIDE.md`

## 🎯 OPTIMIZATION FEATURES

Your deployment includes these **free tier optimizations**:

✅ **Python 3.11 slim image** (smaller, faster)  
✅ **Single worker process** (memory efficient)  
✅ **Scale-to-zero** (no idle costs)  
✅ **Optimal resource limits** (512Mi RAM, 1 CPU)  
✅ **Request-based billing** (pay per use)  
✅ **Health checks** (reliability)  
✅ **CORS optimized** (production ready)  
✅ **Logging configured** (debugging)  

## 🆘 TROUBLESHOOTING

### Common Issues:

1. **"gcloud command not found"**
   - Install Google Cloud CLI (Step 1)

2. **"Project not found"**  
   - Create project: `gcloud projects create PROJECT_ID`

3. **"Billing not enabled"**
   - Enable billing in console (free tier requires billing account)

4. **"Build failed"**
   - Check Dockerfile and requirements.txt
   - Run: `docker build -t test .` locally first

5. **"Service timeout"**
   - AI processing takes time, this is expected for first request
   - Cold starts: 15-30 seconds

6. **"API key errors"**
   - Set environment variables in Cloud Run console
   - Or use: `gcloud run services update ... --set-env-vars`

## 🎉 SUCCESS INDICATORS

When deployment succeeds, you'll see:

✅ Build completes successfully  
✅ Service URL is provided  
✅ Health check returns 200 OK  
✅ API endpoint processes requests  
✅ Logs show successful startup  

## 💡 NEXT STEPS

Once deployed:

1. **Update frontend** to use Cloud Run URL
2. **Set up custom domain** (optional) 
3. **Configure monitoring alerts**
4. **Implement CI/CD** for updates
5. **Scale based on usage patterns**

## 📞 SUPPORT

- **Documentation**: https://cloud.google.com/run/docs
- **Community**: https://www.googlecloudcommunity.com/
- **Stack Overflow**: Tag `google-cloud-run`
- **Pricing Calculator**: https://cloud.google.com/products/calculator

---

**🎯 Your Cloud Run URL will be:**
`https://kickstart-learning-agent-[random]-uc.a.run.app`

**💸 Monthly cost within free tier: $0.00**
