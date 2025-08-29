# Vercel Deployment Guide

## Prerequisites
- Node.js 18 or later
- A Vercel account (https://vercel.com)
- Your Cloud Run backend URL: `https://ai-learning-pathway-428472674191.europe-west1.run.app`

## Quick Deploy

### Option 1: Deploy via Vercel Web Interface

1. **Push your code to GitHub** (if not already done)
2. **Go to Vercel Dashboard** (https://vercel.com/dashboard)
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Configure the project:**
   - Framework Preset: `Vite`
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

6. **Add Environment Variables:**
   - Key: `VITE_API_BASE_URL`
   - Value: `https://ai-learning-pathway-428472674191.europe-west1.run.app`

7. **Deploy!**

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy from the project directory:**
   ```bash
   cd adaptive-learning-agent
   vercel
   ```

4. **Follow the prompts:**
   - Link to existing project? `N`
   - Project name: `adaptive-learning-agent` (or your preferred name)
   - Directory: `./` (current directory)

5. **Add environment variable:**
   ```bash
   vercel env add VITE_API_BASE_URL
   ```
   Enter: `https://ai-learning-pathway-428472674191.europe-west1.run.app`
   Select: Production, Preview, Development

6. **Redeploy with environment variables:**
   ```bash
   vercel --prod
   ```

## Project Structure
```
adaptive-learning-agent/
├── vercel.json          # Vercel configuration
├── vite.config.ts       # Vite configuration with proxy
├── .env.example         # Environment variables template
├── dist/                # Build output directory
└── src/                 # Source code
```

## Environment Variables
- `VITE_API_BASE_URL`: Your Cloud Run backend URL

## API Proxy Configuration
The `vercel.json` file includes API rewrites that proxy `/api/*` requests to your Cloud Run backend, ensuring seamless integration between your frontend and backend.

## Troubleshooting

### CORS Issues
If you encounter CORS issues, make sure your Cloud Run backend includes the Vercel domain in its CORS configuration.

### Build Failures
- Ensure all dependencies are in `package.json`
- Check that the build command `npm run build` works locally
- Verify TypeScript compilation passes

### Environment Variables Not Working
- Make sure environment variables start with `VITE_`
- Restart the deployment after adding environment variables
- Check the Vercel dashboard under Project Settings > Environment Variables

## Testing the Deployment
After deployment, your app will be available at a Vercel URL (e.g., `https://your-app-name.vercel.app`). The API calls will automatically be proxied to your Cloud Run backend.
