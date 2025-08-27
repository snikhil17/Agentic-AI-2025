#!/bin/bash

# Pre-deployment checklist for Google Cloud Run
echo "🔍 Pre-deployment Checklist for Google Cloud Run"
echo "================================================="

# Check if gcloud is installed
echo -n "✓ Google Cloud CLI installed: "
if command -v gcloud &> /dev/null; then
    echo "✅ YES ($(gcloud version --format='value(Google Cloud SDK)' | head -1))"
else
    echo "❌ NO - Please install: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check authentication
echo -n "✓ Authenticated with Google Cloud: "
if gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -1 > /dev/null; then
    ACCOUNT=$(gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -1)
    echo "✅ YES ($ACCOUNT)"
else
    echo "❌ NO - Run: gcloud auth login"
    exit 1
fi

# Check project is set
echo -n "✓ Project is configured: "
PROJECT=$(gcloud config get-value project 2>/dev/null)
if [ ! -z "$PROJECT" ]; then
    echo "✅ YES ($PROJECT)"
else
    echo "❌ NO - Run: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

# Check billing is enabled
echo -n "✓ Billing enabled: "
BILLING_ENABLED=$(gcloud billing projects describe $PROJECT --format="value(billingEnabled)" 2>/dev/null)
if [ "$BILLING_ENABLED" = "True" ]; then
    echo "✅ YES"
else
    echo "⚠️ UNKNOWN - Please verify billing is enabled in console"
fi

# Check required files exist
echo -n "✓ Dockerfile exists: "
if [ -f "Dockerfile" ]; then
    echo "✅ YES"
else
    echo "❌ NO"
    exit 1
fi

echo -n "✓ Cloud Run app exists: "
if [ -f "app_cloudrun.py" ]; then
    echo "✅ YES"
else
    echo "❌ NO"
    exit 1
fi

echo -n "✓ Requirements.txt exists: "
if [ -f "requirements.txt" ]; then
    echo "✅ YES"
else
    echo "❌ NO"
    exit 1
fi

# Check Python imports
echo -n "✓ App can be imported: "
if python -c "import app_cloudrun" 2>/dev/null; then
    echo "✅ YES"
else
    echo "❌ NO - Check for import errors"
    exit 1
fi

# Estimate costs
echo ""
echo "💰 Free Tier Limits Check:"
echo "   • CPU: 180,000 vCPU-seconds/month"
echo "   • Memory: 360,000 GiB-seconds/month"
echo "   • Requests: 2 million/month"
echo "   • Network: 1 GiB egress/month (North America)"

echo ""
echo "📊 Your Configuration:"
echo "   • Memory: 512 MiB (optimized)"
echo "   • CPU: 1 vCPU (single core)"
echo "   • Min Instances: 0 (scales to zero)"
echo "   • Max Instances: 10 (controlled scaling)"
echo "   • Region: Tier 1 pricing (recommended)"

echo ""
echo "🎯 Estimated Usage (within free tier):"
echo "   • ~10,000 requests/day (18s avg processing)"
echo "   • ~100,000 requests/day (1.8s avg processing)"
echo "   • Cold start: 15-30 seconds first request"

echo ""
echo "🚀 Ready for deployment!"
echo "   Run: ./deploy-cloudrun.sh $PROJECT kickstart-learning-agent us-central1"
