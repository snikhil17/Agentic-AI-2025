# Monitoring Your Free Tier Usage

## 📊 Key Metrics to Monitor

### 1. CPU Usage (vCPU-seconds)
- **Limit**: 180,000 vCPU-seconds/month
- **Formula**: CPU allocation × Instance time × Number of instances
- **Example**: 1 vCPU × 60 seconds × 1 instance = 60 vCPU-seconds

### 2. Memory Usage (GiB-seconds)  
- **Limit**: 360,000 GiB-seconds/month
- **Formula**: Memory allocation × Instance time × Number of instances
- **Example**: 0.5 GiB × 60 seconds × 1 instance = 30 GiB-seconds

### 3. Requests
- **Limit**: 2,000,000 requests/month
- **Note**: Only billable requests count (after authentication)

### 4. Network Egress
- **Limit**: 1 GiB/month free (North America)
- **Note**: Response data sent to clients

## 🔍 Monitoring Commands

```bash
# Get current usage (requires billing account access)
gcloud logging read "resource.type=cloud_run_revision" --freshness=1d --format="value(timestamp, severity, textPayload)"

# Check service details
gcloud run services describe kickstart-learning-agent --region=us-central1

# View metrics in console
gcloud run services list --uri | grep kickstart-learning-agent
```

## 📈 Usage Estimation Calculator

### Based on Your App Configuration:
- **Memory**: 512 MiB = 0.5 GiB  
- **CPU**: 1 vCPU
- **Average Request Time**: ~10-15 seconds (AI processing)

### Monthly Limits:
```
CPU Limit: 180,000 vCPU-seconds ÷ 1 vCPU = 180,000 seconds
= 3,000 minutes = 50 hours of processing time

Memory Limit: 360,000 GiB-seconds ÷ 0.5 GiB = 720,000 seconds  
= 12,000 minutes = 200 hours of processing time

Bottleneck: CPU (50 hours < 200 hours)
```

### Request Capacity:
```
With 15-second average processing:
180,000 seconds ÷ 15 seconds/request = 12,000 requests/month

With 5-second average processing:
180,000 seconds ÷ 5 seconds/request = 36,000 requests/month
```

## ⚠️ Usage Alerts

Set up alerts before hitting limits:

### Option 1: Console Alerts
1. Go to [Monitoring](https://console.cloud.google.com/monitoring)
2. Create Alert Policy
3. Set conditions:
   - Resource: Cloud Run
   - Metric: CPU utilization or Request count
   - Threshold: 80% of limit

### Option 2: Budget Alerts  
1. Go to [Billing](https://console.cloud.google.com/billing)
2. Create Budget
3. Set amount: $0.01 (will alert on any charges)

## 🎯 Optimization Strategies

### To Stay Within Free Tier:

1. **Reduce Processing Time**
   - Cache common responses
   - Optimize AI model calls
   - Use async processing where possible

2. **Optimize Memory Usage**
   - Load models lazily
   - Clear unused variables
   - Use memory-efficient data structures

3. **Scale to Zero**
   - Min instances = 0 (no idle costs)
   - Accept cold start latency

4. **Request Batching**
   - Process multiple items per request
   - Reduce total request count

## 📊 Sample Monitoring Script

```bash
#!/bin/bash
# Check current month usage approximation

SERVICE_NAME="kickstart-learning-agent"
REGION="us-central1"

# Get request count (last 30 days approximation)
echo "📈 Approximate Usage (last 30 days):"

# Request count from logs
REQUESTS=$(gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=$SERVICE_NAME" --freshness=30d --format="value(timestamp)" | wc -l)
echo "   Requests: $REQUESTS / 2,000,000 ($(echo "scale=1; $REQUESTS*100/2000000" | bc)%)"

# Service details
gcloud run services describe $SERVICE_NAME --region=$REGION --format="table(
    spec.template.spec.containers[0].resources.limits.memory,
    spec.template.spec.containers[0].resources.limits.cpu,
    spec.template.metadata.annotations[autoscaling.knative.dev/minScale],
    spec.template.metadata.annotations[autoscaling.knative.dev/maxScale]
)"

echo ""
echo "💡 Tips to reduce usage:"
echo "   • Optimize your AI processing pipeline"
echo "   • Cache frequent requests"
echo "   • Use smaller models if possible"
echo "   • Batch multiple queries together"
```

## 🚨 What Happens When You Exceed Free Tier?

1. **CPU/Memory Overuse**: Service continues, charges apply
2. **Request Overuse**: Service continues, charges apply  
3. **Network Overuse**: Service continues, charges apply

**Typical costs beyond free tier:**
- CPU: ~$0.000024 per vCPU-second
- Memory: ~$0.0000025 per GiB-second
- Requests: ~$0.40 per million
- Network: ~$0.12 per GiB

## 💰 Cost Control Measures

```bash
# Set max instances to control costs
gcloud run services update kickstart-learning-agent \
  --region us-central1 \
  --max-instances 5

# Set timeout to prevent long-running requests
gcloud run services update kickstart-learning-agent \
  --region us-central1 \
  --timeout 240s
```
