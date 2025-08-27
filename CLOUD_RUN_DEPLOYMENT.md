# Google Cloud Run Deployment Guide - Free Tier

This guide will help you deploy your Kickstart Learning Agent to Google Cloud Run while staying within the **free tier limits**.

## 🆓 Free Tier Limits
- **CPU**: 180,000 vCPU-seconds per month
- **Memory**: 360,000 GiB-seconds per month  
- **Requests**: 2 million requests per month
- **Network**: 1 GiB free egress per month (North America)

## 📋 Prerequisites

### 1. Install Google Cloud CLI
```bash
# Download and install from: https://cloud.google.com/sdk/docs/install

# Verify installation
gcloud --version
```

### 2. Create Google Cloud Project
```bash
# Create new project (replace with your preferred project ID)
gcloud projects create kickstart-learning-2025 --name="Kickstart Learning Agent"

# Set as default project
gcloud config set project kickstart-learning-2025

# Enable billing (required even for free tier)
# Go to: https://console.cloud.google.com/billing
```

### 3. Authenticate
```bash
# Login to Google Cloud
gcloud auth login

# Set application default credentials
gcloud auth application-default login
```

## 🚀 Quick Deployment

### Option 1: Automated Script (Recommended)
```bash
# Make sure you're in the project root directory
cd kickstart-learning-using-agents

# Run the deployment script
./deploy-cloudrun.sh your-project-id kickstart-learning-agent us-central1
```

### Option 2: Manual Deployment
```bash
# Enable required APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

# Deploy from source (Cloud Build will create the container)
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
  --concurrency 100 \
  --port 8080 \
  --set-env-vars PYTHONUNBUFFERED=1,PORT=8080
```

## 🔧 Configuration for Free Tier

The deployment is optimized for free tier with these settings:

- **Memory**: 512 MiB (keeps within free limits)
- **CPU**: 1 vCPU (single core for efficiency)
- **Min Instances**: 0 (scale to zero when not in use)
- **Max Instances**: 10 (prevent runaway costs)
- **Concurrency**: 100 (handle multiple requests per instance)
- **Timeout**: 240s (sufficient for AI processing)
- **Region**: us-central1 (cheapest Tier 1 pricing)

## 🌍 Environment Variables

For production deployment, set these environment variables:

```bash
# Set API keys in Cloud Run console or via command
gcloud run services update kickstart-learning-agent \
  --region us-central1 \
  --set-env-vars GOOGLE_API_KEY=your_google_api_key,TAVILY_API_KEY=your_tavily_api_key
```

## 📊 Monitor Usage

Track your free tier usage:

1. **Cloud Run Console**: https://console.cloud.google.com/run
2. **Billing**: https://console.cloud.google.com/billing/reports
3. **Metrics**: Click on your service → Metrics tab

## 🔍 Testing Deployment

After deployment, test your endpoints:

```bash
# Get service URL
SERVICE_URL=$(gcloud run services describe kickstart-learning-agent --platform managed --region us-central1 --format 'value(status.url)')

# Test health endpoint
curl $SERVICE_URL/health

# Test API endpoint
curl -X POST $SERVICE_URL/api/generate-pathway-direct \
  -H "Content-Type: application/json" \
  -d '{
    "learning_style": "Interactive examples",
    "progress": "Python basics", 
    "hobby": "Gaming",
    "domain": "Software Development",
    "google_api_key": "your_key",
    "tavily_api_key": "your_key"
  }'
```

## 💰 Cost Optimization Tips

1. **Scale to Zero**: Min instances = 0 (no cost when idle)
2. **Request-based Billing**: Only pay for active requests
3. **Memory Optimization**: 512Mi is optimal for this app
4. **Regional Selection**: Use Tier 1 regions (us-central1, us-east1)
5. **Connection Pooling**: App is optimized for efficient connections

## 🔧 Troubleshooting

### Common Issues:

1. **Cold Starts**: First request may be slow (15-30s)
   - Solution: Consider keeping 1 min instance if needed

2. **Memory Errors**: If 512Mi isn't enough
   - Solution: Increase to 1Gi (still within free tier)

3. **Timeout Errors**: AI processing takes too long
   - Solution: Increase timeout to 900s max

4. **API Key Errors**: Missing environment variables
   - Solution: Set GOOGLE_API_KEY and TAVILY_API_KEY

### Debug Commands:
```bash
# View logs
gcloud logging read "resource.type=cloud_run_revision" --limit 50

# Check service status  
gcloud run services describe kickstart-learning-agent --region us-central1

# Update service
gcloud run services update kickstart-learning-agent --region us-central1 --memory 1Gi
```

## 📈 Scaling Considerations

Within free tier limits, you can handle approximately:
- **~10,000 requests/day** with 18s average processing time
- **~100,000 requests/day** with 1.8s average processing time  
- **2M requests/month** total

## 🔒 Security Features

- **Container runs as non-root user**
- **Python slim image** (reduced attack surface)
- **HTTPS only** (automatic with Cloud Run)
- **CORS configured** for production domains
- **No secrets in image** (use environment variables)

## 🎉 Next Steps

Once deployed:
1. Update your frontend to use the Cloud Run URL
2. Set up custom domain (optional)
3. Configure monitoring alerts
4. Consider CI/CD pipeline for updates

Your application will be available at:
`https://kickstart-learning-agent-[hash]-uc.a.run.app`
