#!/bin/bash

# Deploy to Google Cloud Run - Free Tier Optimized
# This script deploys your FastAPI application to Cloud Run within free tier limits

set -e  # Exit on any error

# Configuration
PROJECT_ID="${1:-your-project-id}"
SERVICE_NAME="${2:-kickstart-learning-agent}"
REGION="${3:-us-central1}"  # Cheapest tier 1 region
APP_FILE="app_cloudrun.py"

echo "🚀 Deploying to Google Cloud Run (Free Tier Optimized)"
echo "Project ID: $PROJECT_ID"
echo "Service Name: $SERVICE_NAME"
echo "Region: $REGION"
echo "App File: $APP_FILE"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI not found. Please install Google Cloud CLI first:"
    echo "   https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -1 > /dev/null; then
    echo "❌ Not authenticated with Google Cloud. Run: gcloud auth login"
    exit 1
fi

# Set the project
echo "📋 Setting Google Cloud project..."
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "🔧 Enabling required APIs..."
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Deploy with free tier optimizations
echo "🏗️ Building and deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --source . \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --max-instances 10 \
    --min-instances 0 \
    --memory 512Mi \
    --cpu 1 \
    --timeout 240s \
    --concurrency 100 \
    --port 8080 \
    --set-env-vars PYTHONUNBUFFERED=1 \
    --set-env-vars PORT=8080 \
    --quiet

# Get the service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)')

echo ""
echo "✅ Deployment completed successfully!"
echo "🌐 Service URL: $SERVICE_URL"
echo "📊 Health Check: $SERVICE_URL/health"
echo "📚 API Docs: $SERVICE_URL/docs"
echo ""
echo "💡 Free Tier Limits:"
echo "   • 180,000 vCPU-seconds/month"
echo "   • 360,000 GiB-seconds/month"  
echo "   • 2 million requests/month"
echo ""
echo "📈 Monitor usage: https://console.cloud.google.com/run/detail/$REGION/$SERVICE_NAME/metrics"
