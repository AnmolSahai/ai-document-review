# Deploying to Vercel

This document outlines the steps to deploy the AI Document Review application to Vercel.

## Prerequisites

1. A Vercel account (https://vercel.com)
2. Git repository with your code
3. Vercel CLI (optional for local testing)

## Recent Changes to Fix Deployment Issues

1. **Reduced Serverless Function Size**:
   - Removed heavy dependencies from `api/requirements.txt`
   - Created a lightweight FastAPI implementation in `api/index.py`

2. **Fixed Frontend Bundle Size Issues**:
   - Added manual chunks configuration in Vite
   - Increased the chunk size warning limit
   - Implemented code splitting for large dependencies

3. **Updated Vercel Configuration**:
   - Added function configuration in `vercel.json` for increased memory and execution time

## Deployment Steps

### 1. Connect Repository to Vercel

1. Log in to your Vercel account
2. Click "Add New" > "Project"
3. Import your Git repository
4. Configure the project:
   - Framework Preset: Other
   - Build Command: `cd app/ui && npm install && npm run build`
   - Output Directory: `app/api/www`
   - Install Command: `npm install`
   - Development Command: `cd app/ui && npm run start`

### 2. Environment Variables

Set up the following environment variables in Vercel's project settings:

```
# Add all environment variables from app/api/.env.tpl
```

### 3. Deploy

Click "Deploy" and Vercel will build and deploy your application.

## Testing the Deployment

After deployment, you can test the application at the provided URL.

- Frontend should be available at the root URL
- API endpoints should be available at `/api/...`
- Health check endpoint is at `/api/health`

## Troubleshooting

- If the API is not working, check the Vercel logs for any errors
- Make sure all environment variables are correctly set
- If you still have issues with function size:
  1. Consider moving to a dedicated server for your backend
  2. Split the application into multiple smaller functions
  3. Use external API services for heavy dependencies

## Local Testing

You can test your Vercel configuration locally using the Vercel CLI:

```bash
npm i -g vercel
vercel dev
``` 